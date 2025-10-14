#!/bin/bash

# Job Recommendation API - Quick Start Script

echo "🚀 Job Recommendation API - Quick Start"
echo "======================================="

# Check if Docker is running
if ! docker info > /dev/null 2>&1; then
    echo "❌ Docker is not running. Please start Docker Desktop first."
    exit 1
fi

# Check if .env exists
if [ ! -f .env ]; then
    echo "📝 Setting up environment..."
    cp .env.example .env
    echo "✅ Environment file created!"
    echo "⚠️  Please edit .env file with your API keys before continuing."
    echo ""
    echo "Required API keys:"
    echo "- OPENAI_API_KEY=your_openai_api_key_here"
    echo "- FIRECRAWL_API_KEY=your_firecrawl_api_key_here"
    echo ""
    read -p "Press Enter after you've updated the .env file..."
fi

# Build and start the application
echo "🔨 Building and starting the application..."
docker compose up -d --build

# Wait for the application to start
echo "⏳ Waiting for the application to start..."
sleep 10

# Check if the application is healthy
echo "🔍 Checking application health..."
if curl -s http://localhost:8000/health > /dev/null; then
    echo "✅ Application is running successfully!"
    echo ""
    echo "📊 Available endpoints:"
    echo "   API: http://localhost:8000"
    echo "   Docs: http://localhost:8000/docs"
    echo "   Health: http://localhost:8000/health"
    echo ""
    echo "🧪 Test the API:"
    echo "   docker compose exec job-recommend-api python test_api.py --demo"
    echo ""
    echo "📋 Useful commands:"
    echo "   View logs: docker compose logs -f"
    echo "   Stop app: docker compose down"
    echo "   Restart: docker compose restart"
else
    echo "❌ Application failed to start. Check logs with: docker compose logs"
fi
