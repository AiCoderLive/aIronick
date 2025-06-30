# Deployment Guide

## Environment Configuration

### Local Development
No additional configuration needed. The application will work with default settings.

### Production Deployment (OVH Server)

1. **Set Base URL Environment Variable**
   
   If your application is served from a subdirectory (e.g., `domain.com/app/`), set the base URL:
   
   ```bash
   export STREAMLIT_BASE_URL="/app"
   ```
   
   Or create a `.env` file:
   ```
   STREAMLIT_BASE_URL="/app"
   ENVIRONMENT="production"
   ```

2. **Docker Deployment**
   
   Update your docker-compose.yml or Docker run command:
   ```yaml
   environment:
     - STREAMLIT_BASE_URL=/your-app-path
     - ENVIRONMENT=production
   ```

3. **Direct Streamlit Deployment**
   
   If running Streamlit directly:
   ```bash
   export STREAMLIT_BASE_URL="/your-app-path"
   streamlit run app.py
   ```

## Reverse Proxy Configuration

### Nginx Configuration
```nginx
location /your-app-path/ {
    proxy_pass http://localhost:8501/;
    proxy_set_header Host $host;
    proxy_set_header X-Real-IP $remote_addr;
    proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
    proxy_set_header X-Forwarded-Proto $scheme;
    
    # WebSocket support for Streamlit
    proxy_http_version 1.1;
    proxy_set_header Upgrade $http_upgrade;
    proxy_set_header Connection "upgrade";
}
```

### Apache Configuration
```apache
ProxyPreserveHost On
ProxyPass /your-app-path/ http://localhost:8501/
ProxyPassReverse /your-app-path/ http://localhost:8501/

# WebSocket support
RewriteEngine On
RewriteCond %{HTTP:Upgrade} websocket [NC]
RewriteCond %{HTTP:Connection} upgrade [NC]
RewriteRule ^/your-app-path/(.*) "ws://localhost:8501/$1" [P,L]
```

## Testing the Deployment

1. **Test Navigation**
   - Homepage should load correctly
   - "Zobacz więcej" button should navigate to testing page
   - Back button should return to homepage
   - Navbar navigation should work from both pages

2. **Test URL Patterns**
   - Direct access to `yoursite.com/your-app-path/?page=testowanie_oprogramowania`
   - Browser refresh should maintain current page state
   - All internal links should resolve correctly

## Troubleshooting

### Common Issues

1. **Navigation not working**: Check if `STREAMLIT_BASE_URL` is correctly set
2. **404 errors**: Verify reverse proxy configuration
3. **WebSocket errors**: Ensure WebSocket support is enabled in your proxy
4. **Mixed content warnings**: Make sure HTTPS is properly configured

### Debug Mode

Enable debug logging by setting:
```bash
export STREAMLIT_LOGGER_LEVEL=debug
```

## URL Helper Features

The application now uses a centralized URL helper that:
- Automatically detects the base URL from environment or Streamlit config
- Provides consistent URL generation across all components
- Handles both old and new Streamlit query parameter APIs
- Ensures compatibility across different deployment scenarios