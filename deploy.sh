#!/bin/bash

# Configuration
REPO_DIR="/home/ubuntu/aironick"
CONTAINER_NAME="aironick"
IMAGE_NAME="aironick-app"

cd $REPO_DIR

echo "🔄 Pulling latest code..."
git pull origin main

echo "🛑 Stopping old container..."
sudo docker stop $CONTAINER_NAME 2>/dev/null || true
sudo docker rm $CONTAINER_NAME 2>/dev/null || true

echo "🏗️ Building new image..."
sudo docker build -t $IMAGE_NAME .

echo "📁 Checking for .env file..."
if [ -f ".env" ]; then
    echo "✅ Found .env file - loading environment variables"
    source .env
else
    echo "⚠️ No .env file found - using default configuration"
fi

echo "🚀 Starting new container..."
sudo docker run -d \
    -p 8501:8501 \
    --name $CONTAINER_NAME \
    --restart unless-stopped \
    -e STREAMLIT_SERVER_PORT=8501 \
    -e STREAMLIT_SERVER_ADDRESS=0.0.0.0 \
    -e STREAMLIT_BASE_URL="${STREAMLIT_BASE_URL:-}" \
    -e ENVIRONMENT="${ENVIRONMENT:-production}" \
    $IMAGE_NAME

echo "🔍 Checking container status..."
sudo docker ps | grep $CONTAINER_NAME

echo "📋 Recent logs:"
sudo docker logs --tail 10 $CONTAINER_NAME

echo "🌐 Application should be available at:"
if [ -n "$STREAMLIT_BASE_URL" ]; then
    echo "   http://your-domain.com$STREAMLIT_BASE_URL"
else
    echo "   http://your-domain.com:8501"
fi

echo "✅ Deployment complete!"

# Optional: Test if the application is responding
echo "🧪 Testing application health..."
sleep 5
if curl -f -s http://localhost:8501 > /dev/null; then
    echo "✅ Application is responding"
else
    echo "❌ Application may not be responding - check logs:"
    sudo docker logs --tail 20 $CONTAINER_NAME
fi