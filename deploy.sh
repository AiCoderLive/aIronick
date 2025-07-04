#!/bin/bash

# aIRONick Deployment Script
# This script handles complete deployment/update of the application

set -e  # Exit on any error

# Colors for output
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
BLUE='\033[0;34m'
NC='\033[0m' # No Color

# Configuration
PROJECT_NAME="aironick"
COMPOSE_FILE="docker-compose.yml"
GIT_REPO="https://github.com/AiCoderLive/aIronick.git"  # Update this with your repo URL
BRANCH="main"  # or master, depending on your default branch
BACKUP_DIR="backups"
LOG_FILE="deploy.log"

# Function to print colored output
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

# Function to log messages
log_message() {
    echo "$(date '+%Y-%m-%d %H:%M:%S') - $1" >> "$LOG_FILE"
}

# Function to check if command exists
command_exists() {
    command -v "$1" >/dev/null 2>&1
}

# Function to check prerequisites
check_prerequisites() {
    print_status "Checking prerequisites..."

    if ! command_exists docker; then
        print_error "Docker is not installed. Please install Docker first."
        exit 1
    fi

    if ! command_exists docker-compose; then
        print_error "Docker Compose is not installed. Please install Docker Compose first."
        exit 1
    fi

    if ! command_exists git; then
        print_error "Git is not installed. Please install Git first."
        exit 1
    fi

    print_success "Prerequisites check passed"
}

# Function to create backup
create_backup() {
    print_status "Creating backup..."

    # Create backup directory if it doesn't exist
    mkdir -p "$BACKUP_DIR"

    # Create timestamp for backup
    TIMESTAMP=$(date '+%Y%m%d_%H%M%S')
    BACKUP_NAME="${PROJECT_NAME}_backup_${TIMESTAMP}"

    # Backup current docker-compose.yml and important files
    if [ -f "$COMPOSE_FILE" ]; then
        cp "$COMPOSE_FILE" "$BACKUP_DIR/${BACKUP_NAME}_docker-compose.yml"
        log_message "Backed up docker-compose.yml"
    fi

    # Backup any custom configuration files
    if [ -f "nginx.conf" ]; then
        cp "nginx.conf" "$BACKUP_DIR/${BACKUP_NAME}_nginx.conf"
        log_message "Backed up nginx.conf"
    fi

    print_success "Backup created in $BACKUP_DIR"
}

# Function to stop and remove containers
cleanup_containers() {
    print_status "Stopping and removing containers..."

    # Stop all containers for this project
    if docker-compose ps -q 2>/dev/null | grep -q .; then
        docker-compose down --remove-orphans
        log_message "Stopped and removed containers"
    else
        print_warning "No containers to stop"
    fi

    # Remove any dangling containers
    if docker ps -a --filter "name=${PROJECT_NAME}" -q | grep -q .; then
        docker ps -a --filter "name=${PROJECT_NAME}" -q | xargs docker rm -f
        log_message "Removed dangling containers"
    fi

    print_success "Container cleanup completed"
}

# Function to clean up Docker resources
cleanup_docker() {
    print_status "Cleaning up Docker resources..."

    # Remove unused images
    docker image prune -f

    # Remove unused volumes
    docker volume prune -f

    # Remove unused networks
    docker network prune -f

    log_message "Docker cleanup completed"
    print_success "Docker resources cleaned up"
}

# Function to update code from git
update_code() {
    print_status "Updating code from Git..."

    # Check if this is a git repository
    if [ -d ".git" ]; then
        # Stash any local changes
        git stash push -m "Deploy script stash $(date)"

        # Pull latest changes
        git fetch origin
        git reset --hard origin/$BRANCH

        log_message "Code updated from Git"
        print_success "Code updated from repository"
    else
        print_warning "Not a git repository. Skipping code update."
        print_warning "Make sure you have the latest code manually."
    fi
}

# Function to build and start containers
build_and_start() {
    print_status "Building and starting containers..."

    # Build containers
    docker-compose build --no-cache
    log_message "Docker images built"

    # Start containers
    docker-compose up -d
    log_message "Containers started"

    print_success "Application built and started"
}

# Function to wait for application to be ready
wait_for_app() {
    print_status "Waiting for application to be ready..."

    # Wait for the application to be healthy
    MAX_ATTEMPTS=30
    ATTEMPT=1

    while [ $ATTEMPT -le $MAX_ATTEMPTS ]; do
        if curl -f -s http://localhost:8501/health >/dev/null 2>&1; then
            print_success "Application is ready!"
            return 0
        fi

        print_status "Attempt $ATTEMPT/$MAX_ATTEMPTS - Waiting for application..."
        sleep 5
        ATTEMPT=$((ATTEMPT + 1))
    done

    print_error "Application failed to start within expected time"
    return 1
}

# Function to show application status
show_status() {
    print_status "Application Status:"
    echo "===================="

    # Show container status
    docker-compose ps

    echo ""
    print_status "Application URLs:"
    echo "Development: http://localhost:8501"
    echo "Health Check: http://localhost:8501/health"

    # Show logs
    echo ""
    print_status "Recent logs:"
    docker-compose logs --tail=10
}

# Function to show help
show_help() {
    echo "aIRONick Deployment Script"
    echo "========================="
    echo ""
    echo "Usage: $0 [OPTIONS]"
    echo ""
    echo "Options:"
    echo "  -h, --help          Show this help message"
    echo "  -f, --force         Force deployment without confirmation"
    echo "  -n, --no-backup     Skip backup creation"
    echo "  -c, --cleanup-only  Only cleanup containers and exit"
    echo "  -b, --build-only    Only build containers without starting"
    echo "  --no-git            Skip git update"
    echo ""
    echo "Examples:"
    echo "  $0                  # Normal deployment with all steps"
    echo "  $0 -f               # Force deployment without confirmation"
    echo "  $0 -c               # Only cleanup containers"
    echo "  $0 --no-git         # Deploy without updating from git"
}

# Parse command line arguments
FORCE=false
NO_BACKUP=false
CLEANUP_ONLY=false
BUILD_ONLY=false
NO_GIT=false

while [[ $# -gt 0 ]]; do
    case $1 in
        -h|--help)
            show_help
            exit 0
            ;;
        -f|--force)
            FORCE=true
            shift
            ;;
        -n|--no-backup)
            NO_BACKUP=true
            shift
            ;;
        -c|--cleanup-only)
            CLEANUP_ONLY=true
            shift
            ;;
        -b|--build-only)
            BUILD_ONLY=true
            shift
            ;;
        --no-git)
            NO_GIT=true
            shift
            ;;
        *)
            print_error "Unknown option: $1"
            show_help
            exit 1
            ;;
    esac
done

# Main deployment function
main() {
    print_status "Starting aIRONick deployment..."
    echo "========================================"
    log_message "Deployment started"

    # Check prerequisites
    check_prerequisites

    # Show confirmation unless forced
    if [ "$FORCE" = false ]; then
        echo ""
        print_warning "This will stop current containers and redeploy the application."
        read -p "Do you want to continue? (y/N): " -n 1 -r
        echo
        if [[ ! $REPLY =~ ^[Yy]$ ]]; then
            print_status "Deployment cancelled"
            exit 0
        fi
    fi

    # Create backup
    if [ "$NO_BACKUP" = false ]; then
        create_backup
    fi

    # Stop and remove containers
    cleanup_containers

    # Clean up Docker resources
    cleanup_docker

    # Exit if cleanup only
    if [ "$CLEANUP_ONLY" = true ]; then
        print_success "Cleanup completed"
        exit 0
    fi

    # Update code from git
    if [ "$NO_GIT" = false ]; then
        update_code
    fi

    # Build and start containers
    build_and_start

    # Exit if build only
    if [ "$BUILD_ONLY" = true ]; then
        print_success "Build completed"
        exit 0
    fi

    # Wait for application to be ready
    if wait_for_app; then
        show_status
        echo ""
        print_success "🚀 Deployment completed successfully!"
        print_success "Application is running at: http://localhost:8501"
        log_message "Deployment completed successfully"
    else
        print_error "❌ Deployment failed - Application is not responding"
        print_status "Check logs with: docker-compose logs"
        log_message "Deployment failed"
        exit 1
    fi
}

# Trap to handle script interruption
trap 'print_error "Deployment interrupted"; exit 1' INT TERM

# Run main function
main "$@"