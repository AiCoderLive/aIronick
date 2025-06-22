#!/bin/bash

echo "Starting aIRONick application..."

# Check if Docker is running
if ! docker info >/dev/null 2>&1; then
    echo "Docker is not running. Please start Docker first."
    exit 1
fi

# Build and start the application
echo "Building Docker image..."
sudo docker compose build

echo "Starting container..."
sudo docker compose up -d

echo "Application started successfully!"
echo "Access the application at: http://localhost:8501"

# Show container status
echo ""
echo "Container status:"
sudo docker compose ps