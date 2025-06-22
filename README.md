# aIRONick - AI-Powered Streamlit Application

A modern, single-scroll Streamlit application with a sleek design inspired by AI and technology themes.

## Features

- **Single Scroll Design**: Smooth, modern single-page application
- **Top Navigation Menu**: Fixed navigation bar with smooth scrolling
- **Interactive Analytics**: Real-time charts and metrics
- **Responsive Design**: Mobile-friendly layout
- **Docker Ready**: Fully containerized application

## Quick Start

### Prerequisites

- Docker and Docker Compose installed
- Ubuntu 24.04 or compatible Linux distribution

### Running with Docker (Recommended)

1. **Start the application:**
   ```bash
   ./start.sh
   ```

2. **Access the application:**
   Open your web browser and navigate to: `http://localhost:8501`

3. **Stop the application:**
   ```bash
   ./stop.sh
   ```

### Manual Docker Commands

If you prefer to run Docker commands manually:

```bash
# Build the image
sudo docker compose build

# Start the container
sudo docker compose up -d

# Check status
sudo docker compose ps

# View logs
sudo docker compose logs

# Stop the container
sudo docker compose down

# Remove all docker containers
docker rm -f $(docker ps -aq)
```

### Running Locally (Alternative)

If Docker is not available, you can run the application locally:

```bash
# Install dependencies
pip install -r requirements.txt

# Run the application
streamlit run app.py
```

## Application Sections

- **Home**: Hero section with introduction
- **Features**: Key application features
- **Analytics**: Interactive dashboard with metrics and charts
- **About**: Information about the application
- **Contact**: Contact form and information

## Configuration

The application runs on port 8501 by default. You can modify the port in:
- `docker-compose.yml` for Docker deployment
- Run `streamlit run app.py --server.port=XXXX` for local deployment

## Technology Stack

- **Python 3.11**
- **Streamlit 1.28.0**
- **Plotly 5.15.0** (for interactive charts)
- **Pandas 2.1.0** (for data handling)
- **Docker** (for containerization)

## Design Features

- Gradient backgrounds with purple/blue theme
- Hover effects and smooth transitions
- Mobile-responsive design
- Modern card-based layout
- Interactive charts and metrics

## Troubleshooting

### Docker Permission Issues
If you encounter Docker permission errors, ensure your user is in the docker group:
```bash
sudo usermod -aG docker $USER
```
Then log out and log back in.

### Port Already in Use
If port 8501 is already in use, modify the port mapping in `docker-compose.yml`:
```yaml
ports:
  - "8502:8501"  # Change 8502 to your preferred port
```

### Dependencies Issues
If you have dependency conflicts, use a virtual environment:
```bash
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
streamlit run app.py
```

## Support

For issues or questions, please refer to the application's contact section or create an issue in the project repository.