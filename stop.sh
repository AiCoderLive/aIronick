#!/bin/bash

echo "Stopping aIRONick application..."

# Stop and remove containers
sudo docker compose down

echo "Application stopped successfully!"