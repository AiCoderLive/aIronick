#!/bin/bash

# SSL Setup Script for aIRONick
# This script helps set up SSL certificates for your domain

set -e

# Configuration
DOMAIN="aironick.eu"
EMAIL="kontakt@airack.eu"
WEBROOT="/var/www/certbot"

# Colors for output
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
BLUE='\033[0;34m'
NC='\033[0m' # No Color

print_status() {
    echo -e "${BLUE}[INFO]${NC} $1"
}

print_success() {
    echo -e "${GREEN}[SUCCESS]${NC} $1"
}

print_warning() {
    echo -e "${YELLOW}[WARNING]${NC} $1"
}

print_error() {
    echo -e "${RED}[ERROR]${NC} $1"
}

# Function to check if domain is pointing to this server
check_domain() {
    print_status "Checking domain configuration..."

    # Get current public IP
    PUBLIC_IP=$(curl -s ifconfig.me || curl -s ipinfo.io/ip || echo "unknown")

    # Check if domain resolves to this server
    DOMAIN_IP=$(dig +short $DOMAIN || echo "unknown")
    WWW_DOMAIN_IP=$(dig +short www.$DOMAIN || echo "unknown")

    print_status "Your server IP: $PUBLIC_IP"
    print_status "Domain $DOMAIN resolves to: $DOMAIN_IP"
    print_status "Domain www.$DOMAIN resolves to: $WWW_DOMAIN_IP"

    if [ "$PUBLIC_IP" != "$DOMAIN_IP" ] && [ "$PUBLIC_IP" != "$WWW_DOMAIN_IP" ]; then
        print_warning "Domain may not be pointing to this server"
        print_warning "Please ensure your DNS records are correct"
        print_warning "Both $DOMAIN and www.$DOMAIN should point to $PUBLIC_IP"
    else
        print_success "Domain is correctly pointing to this server"
    fi
}

# Function to create initial nginx config without SSL
create_initial_nginx_config() {
    print_status "Creating initial nginx configuration..."

    cat > nginx-initial.conf << 'EOF'
events {
    worker_connections 1024;
}

http {
    include /etc/nginx/mime.types;
    default_type application/octet-stream;

    upstream webapp {
        server webapp:8000;
    }

    server {
        listen 80;
        server_name aironick.eu www.aironick.eu;

        # Let's Encrypt challenge
        location /.well-known/acme-challenge/ {
            root /var/www/certbot;
        }

        # Serve static files
        location /static/ {
            alias /app/static/;
        }

        # Temporary: serve the app over HTTP for certificate generation
        location / {
            proxy_pass http://webapp;
            proxy_set_header Host $host;
            proxy_set_header X-Real-IP $remote_addr;
            proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
            proxy_set_header X-Forwarded-Proto $scheme;
        }
    }
}
EOF
    print_success "Initial nginx configuration created"
}

# Function to check if SSL certificates exist
check_certificates() {
    if [ -d "/etc/letsencrypt/live/$DOMAIN" ]; then
        return 0
    else
        return 1
    fi
}

# Function to setup SSL certificates
setup_ssl() {
    print_status "Setting up SSL certificates for $DOMAIN..."

    # Check if certificates already exist
    if check_certificates; then
        print_warning "SSL certificates already exist for $DOMAIN"
        read -p "Do you want to renew them? (y/N): " -n 1 -r
        echo
        if [[ ! $REPLY =~ ^[Yy]$ ]]; then
            print_status "Skipping SSL setup"
            return 0
        fi
    fi

    # Create directories
    sudo mkdir -p /etc/letsencrypt
    sudo mkdir -p /var/www/certbot

    # Start with initial nginx config
    create_initial_nginx_config

    # Backup existing nginx config
    if [ -f "nginx.conf" ]; then
        cp nginx.conf nginx.conf.backup
        print_status "Backed up existing nginx.conf"
    fi

    # Use initial config
    cp nginx-initial.conf nginx.conf

    # Stop any running containers
    print_status "Stopping existing containers..."
    docker-compose down 2>/dev/null || true

    # Start containers
    print_status "Starting containers for SSL setup..."
    docker-compose up -d nginx webapp

    # Wait for nginx to be ready
    print_status "Waiting for nginx to be ready..."
    sleep 10

    # Check if containers are running
    if ! docker-compose ps | grep -q "Up"; then
        print_error "Containers failed to start"
        return 1
    fi

    # Generate SSL certificate
    print_status "Generating SSL certificate for $DOMAIN and www.$DOMAIN..."
    print_status "Using email: $EMAIL"

    docker-compose run --rm --entrypoint "\
        certbot certonly --webroot -w /var/www/certbot \
        -d $DOMAIN -d www.$DOMAIN \
        --email $EMAIL \
        --agree-tos \
        --non-interactive \
        --expand --force-renewal" certbot

    if [ $? -eq 0 ]; then
        print_success "SSL certificate generated successfully"

        # Restore full nginx config
        if [ -f "nginx.conf.backup" ]; then
            cp nginx.conf.backup nginx.conf
            print_status "Restored full nginx configuration"
        fi

        # Restart nginx to pick up the new config
        docker-compose restart nginx

        print_success "SSL setup completed successfully!"
        print_status "Your site should now be available at https://$DOMAIN"

        # Clean up
        rm -f nginx-initial.conf

    else
        print_error "SSL certificate generation failed"
        # Restore original config if backup exists
        if [ -f "nginx.conf.backup" ]; then
            cp nginx.conf.backup nginx.conf
            print_status "Restored original nginx configuration"
        fi
        return 1
    fi
}

# Function to renew SSL certificates
renew_ssl() {
    print_status "Renewing SSL certificates..."

    if ! check_certificates; then
        print_error "No SSL certificates found. Please run setup first."
        return 1
    fi

    docker-compose run --rm certbot renew

    if [ $? -eq 0 ]; then
        docker-compose restart nginx
        print_success "SSL certificates renewed successfully"
    else
        print_error "SSL renewal failed"
        return 1
    fi
}

# Function to setup auto-renewal
setup_auto_renewal() {
    print_status "Setting up auto-renewal..."

    # Get current directory
    CURRENT_DIR=$(pwd)

    # Create renewal script
    cat > /tmp/renew-ssl.sh << EOF
#!/bin/bash
cd $CURRENT_DIR
docker-compose run --rm certbot renew
docker-compose restart nginx
EOF

    # Make it executable
    chmod +x /tmp/renew-ssl.sh

    # Move to a permanent location
    sudo mv /tmp/renew-ssl.sh /usr/local/bin/aironick-ssl-renew.sh

    # Add to crontab (run twice a month)
    print_status "Adding cron job for auto-renewal..."
    (crontab -l 2>/dev/null | grep -v "aironick-ssl-renew"; echo "0 12 1,15 * * /usr/local/bin/aironick-ssl-renew.sh >> /var/log/ssl-renew.log 2>&1") | crontab -

    print_success "Auto-renewal setup complete"
    print_status "SSL certificates will be renewed automatically on 1st and 15th of each month"
}

# Function to check SSL status
check_ssl() {
    print_status "Checking SSL certificate status..."

    if check_certificates; then
        print_success "SSL certificate found for $DOMAIN"

        # Check expiry
        EXPIRY=$(sudo openssl x509 -enddate -noout -in "/etc/letsencrypt/live/$DOMAIN/fullchain.pem" | cut -d= -f2)
        print_status "Certificate expires: $EXPIRY"

        # Check days until expiry
        EXPIRY_DATE=$(date -d "$EXPIRY" +%s)
        CURRENT_DATE=$(date +%s)
        DAYS_UNTIL_EXPIRY=$(( ($EXPIRY_DATE - $CURRENT_DATE) / 86400 ))

        if [ $DAYS_UNTIL_EXPIRY -lt 30 ]; then
            print_warning "Certificate expires in $DAYS_UNTIL_EXPIRY days - consider renewing"
        else
            print_success "Certificate is valid for $DAYS_UNTIL_EXPIRY more days"
        fi

        # Test SSL connection
        print_status "Testing SSL connection..."
        if curl -s -I "https://$DOMAIN" | grep -q "200 OK"; then
            print_success "HTTPS is working correctly for $DOMAIN"
        else
            print_warning "HTTPS may not be working correctly for $DOMAIN"
        fi

        if curl -s -I "https://www.$DOMAIN" | grep -q "200 OK"; then
            print_success "HTTPS is working correctly for www.$DOMAIN"
        else
            print_warning "HTTPS may not be working correctly for www.$DOMAIN"
        fi
    else
        print_error "SSL certificate not found for $DOMAIN"
        print_status "Run option 2 to set up SSL certificates"
    fi
}

# Function to show current configuration
show_config() {
    print_status "Current SSL configuration:"
    echo "=========================="
    echo "Domain: $DOMAIN"
    echo "WWW Domain: www.$DOMAIN"
    echo "Email: $EMAIL"
    echo "Webroot: $WEBROOT"
    echo "Project Directory: $(pwd)"
    echo ""

    # Show container status
    print_status "Container status:"
    docker-compose ps 2>/dev/null || echo "No containers running"
}

# Main menu
show_menu() {
    echo ""
    echo "SSL Setup for aIRONick ($DOMAIN)"
    echo "================================="
    echo "1. Check domain configuration"
    echo "2. Setup SSL certificates (first time)"
    echo "3. Renew SSL certificates"
    echo "4. Setup auto-renewal"
    echo "5. Check SSL status"
    echo "6. Show current configuration"
    echo "7. Exit"
    echo ""
}

# Main function
main() {
    print_status "SSL Setup Script for aIRONick"
    print_status "Domain: $DOMAIN"
    print_status "Email: $EMAIL"

    while true; do
        show_menu
        read -p "Choose an option (1-7): " choice

        case $choice in
            1)
                check_domain
                ;;
            2)
                setup_ssl
                ;;
            3)
                renew_ssl
                ;;
            4)
                setup_auto_renewal
                ;;
            5)
                check_ssl
                ;;
            6)
                show_config
                ;;
            7)
                print_success "Goodbye!"
                exit 0
                ;;
            *)
                print_error "Invalid option"
                ;;
        esac

        echo ""
        read -p "Press Enter to continue..."
    done
}

# Run main function
main