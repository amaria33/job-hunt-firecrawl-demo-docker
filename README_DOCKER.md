# Job Recommendation API - Docker Setup

This guide will help you run the Job Recommendation API using Docker and Docker Compose.

## 🐳 Prerequisites

- Docker (version 20.10 or higher)
- Docker Compose (version 2.0 or higher)
- Git

## 🚀 Quick Start

### 1. Clone and Setup Environment

```bash
# Clone the repository
git clone <your-repo-url>
cd job-recommend

# Copy environment template
cp .env.example .env

# Edit .env file with your API keys
nano .env
```

### 2. Configure Environment Variables

Edit `.env` file with your actual API keys:

```env
OPENAI_API_KEY=sk-proj-your-actual-openai-key
FIRECRAWL_API_KEY=fc-your-actual-firecrawl-key
```

### 3. Build and Run

```bash
# Build and start the application
docker-compose up --build

# Or run in detached mode
docker-compose up -d --build
```

### 4. Access the Application

- **API**: http://localhost:8000
- **Interactive Docs**: http://localhost:8000/docs
- **Health Check**: http://localhost:8000/health

## 📋 Available Commands

### Development

```bash
# Start the application
docker-compose up

# Start with build
docker-compose up --build

# Start in background
docker-compose up -d

# View logs
docker-compose logs -f

# Stop the application
docker-compose down

# Stop and remove volumes
docker-compose down -v
```

### Production (with Nginx)

```bash
# Start with Nginx reverse proxy
docker-compose --profile production up -d

# View logs for all services
docker-compose logs -f

# Scale the API service
docker-compose up -d --scale job-recommend-api=3
```

### Maintenance

```bash
# Rebuild without cache
docker-compose build --no-cache

# Update dependencies
docker-compose exec job-recommend-api pip install --upgrade -r requirements.txt

# Access container shell
docker-compose exec job-recommend-api bash

# Run tests inside container
docker-compose exec job-recommend-api python test_api.py --demo
```

## 🏗️ Docker Architecture

### Services

1. **job-recommend-api**: Main FastAPI application
2. **nginx** (optional): Reverse proxy for production

### Network

- **job-recommend-network**: Internal network for service communication

### Volumes

- **logs**: Persistent log storage

## 🔧 Configuration

### Environment Variables

| Variable | Description | Default | Required |
|----------|-------------|---------|----------|
| `OPENAI_API_KEY` | OpenAI API key | - | ✅ Yes |
| `FIRECRAWL_API_KEY` | Firecrawl API key | - | ✅ Yes |
| `APP_NAME` | Application name | Job Recommendation API | ❌ No |
| `DEBUG` | Debug mode | false | ❌ No |
| `HOST` | Bind host | 0.0.0.0 | ❌ No |
| `PORT` | Bind port | 8000 | ❌ No |

### Ports

- **8000**: FastAPI application
- **80**: Nginx (production mode)
- **443**: Nginx HTTPS (production mode)

## 🧪 Testing

### Test the API

```bash
# Quick demo test
docker-compose exec job-recommend-api python test_api.py --demo

# Full test suite
docker-compose exec job-recommend-api python test_api.py

# Test with curl
curl http://localhost:8000/health
```

### Test with Sample Request

```bash
curl -X POST "http://localhost:8000/recommend-jobs-demo" \
     -H "Content-Type: application/json" \
     -d '{
       "resume_text": "Software Engineer with 5 years experience in Python, FastAPI, and data analysis. Strong background in system optimization and team collaboration.",
       "num_jobs": 3,
       "num_recommendations": 2
     }'
```

## 📊 Monitoring

### Health Checks

The application includes built-in health checks:

- **Container Health**: Docker health check every 30 seconds
- **API Health**: `/health` endpoint for application status
- **Service Health**: Docker Compose health checks

### Logs

```bash
# View application logs
docker-compose logs job-recommend-api

# Follow logs in real-time
docker-compose logs -f job-recommend-api

# View logs with timestamps
docker-compose logs -t job-recommend-api
```

## 🚀 Production Deployment

### 1. SSL Configuration

```bash
# Create SSL directory
mkdir ssl

# Add your SSL certificates
cp your-cert.pem ssl/cert.pem
cp your-key.pem ssl/key.pem

# Update nginx.conf with your domain
# Uncomment and configure HTTPS server block
```

### 2. Environment Configuration

```bash
# Production environment
cp .env.example .env.production

# Edit production settings
nano .env.production

# Use production environment
docker-compose --env-file .env.production up -d
```

### 3. Deploy with Production Profile

```bash
# Start with Nginx
docker-compose --profile production up -d

# Scale API service
docker-compose up -d --scale job-recommend-api=3
```

## 🛠️ Troubleshooting

### Common Issues

1. **Port Already in Use**
   ```bash
   # Check what's using port 8000
   lsof -i :8000
   
   # Kill the process or change port in docker-compose.yml
   ```

2. **API Keys Not Working**
   ```bash
   # Check environment variables
   docker-compose exec job-recommend-api env | grep API_KEY
   
   # Verify .env file
   cat .env
   ```

3. **Container Won't Start**
   ```bash
   # Check logs
   docker-compose logs job-recommend-api
   
   # Rebuild without cache
   docker-compose build --no-cache
   ```

4. **Health Check Failing**
   ```bash
   # Check if application is running
   docker-compose exec job-recommend-api curl localhost:8000/health
   
   # Check container health
   docker ps
   ```

### Debug Mode

```bash
# Run in debug mode
docker-compose up --build

# Access container for debugging
docker-compose exec job-recommend-api bash

# Install debugging tools
docker-compose exec job-recommend-api pip install ipdb
```

## 📁 File Structure

```
job-recommend/
├── Dockerfile              # Docker image definition
├── docker-compose.yml      # Docker Compose configuration
├── .dockerignore          # Docker build ignore file
├── .gitignore             # Git ignore file
├── .env.example           # Environment variables template
├── nginx.conf             # Nginx configuration
├── app.py                 # FastAPI application
├── models.py              # Pydantic models
├── services.py            # Business logic
├── requirements.txt       # Python dependencies
├── test_api.py           # API tests
└── README_DOCKER.md      # This file
```

## 🔐 Security Notes

- Never commit `.env` files to version control
- Use strong API keys and rotate them regularly
- Enable HTTPS in production
- Configure proper CORS origins
- Use secrets management for production deployments
- Regularly update base images for security patches

## 📞 Support

If you encounter any issues:

1. Check the logs: `docker-compose logs -f`
2. Verify environment variables: `docker-compose exec job-recommend-api env`
3. Test the health endpoint: `curl http://localhost:8000/health`
4. Check Docker status: `docker ps` and `docker-compose ps`
