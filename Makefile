# Job Recommendation API - Docker Management

.PHONY: help build up down logs test clean restart shell status

# Default target
help: ## Show this help message
	@echo "Job Recommendation API - Docker Management"
	@echo "=========================================="
	@echo ""
	@echo "Available commands:"
	@grep -E '^[a-zA-Z_-]+:.*?## .*$$' $(MAKEFILE_LIST) | sort | awk 'BEGIN {FS = ":.*?## "}; {printf "  \033[36m%-15s\033[0m %s\n", $$1, $$2}'

# Environment setup
setup: ## Setup environment from template
	@echo "Setting up environment..."
	@cp .env.example .env
	@echo "✅ Environment file created!"
	@echo "📝 Please edit .env file with your API keys"

# Docker commands
build: ## Build Docker images
	@echo "Building Docker images..."
	docker compose build

up: ## Start the application
	@echo "Starting Job Recommendation API..."
	docker compose up -d

up-build: ## Build and start the application
	@echo "Building and starting Job Recommendation API..."
	docker compose up -d --build

down: ## Stop the application
	@echo "Stopping Job Recommendation API..."
	docker compose down

restart: ## Restart the application
	@echo "Restarting Job Recommendation API..."
	docker compose restart

# Production commands
up-prod: ## Start with production profile (includes Nginx)
	@echo "Starting Job Recommendation API in production mode..."
	docker compose --profile production up -d

down-prod: ## Stop production services
	@echo "Stopping production services..."
	docker compose --profile production down

# Logging and monitoring
logs: ## Show application logs
	docker compose logs -f job-recommend-api

logs-all: ## Show logs for all services
	docker compose logs -f

status: ## Show container status
	@echo "Container Status:"
	@docker compose ps

health: ## Check application health
	@echo "Checking application health..."
	@curl -s http://localhost:8000/health | jq . || echo "❌ Health check failed"

# Development commands
shell: ## Access application container shell
	docker compose exec job-recommend-api bash

test: ## Run API tests
	@echo "Running API tests..."
	docker compose exec job-recommend-api python test_api.py --demo

test-full: ## Run full test suite
	@echo "Running full test suite..."
	docker compose exec job-recommend-api python test_api.py

# Maintenance commands
clean: ## Clean up Docker resources
	@echo "Cleaning up Docker resources..."
	docker compose down -v --remove-orphans
	docker system prune -f

clean-all: ## Clean up all Docker resources (including images)
	@echo "Cleaning up all Docker resources..."
	docker compose down -v --remove-orphans --rmi all
	docker system prune -af

# Database commands (for future use)
db-shell: ## Access database shell (when implemented)
	@echo "Database shell not implemented yet"

db-migrate: ## Run database migrations (when implemented)
	@echo "Database migrations not implemented yet"

# Utility commands
env-check: ## Check environment variables
	@echo "Checking environment variables..."
	@docker compose exec job-recommend-api env | grep -E "(OPENAI|FIRECRAWL|APP_)" || echo "❌ Environment variables not found"

install-deps: ## Install/update dependencies
	@echo "Installing/updating dependencies..."
	docker compose exec job-recommend-api pip install --upgrade -r requirements.txt

# Quick start commands
dev: setup build up ## Quick development setup
	@echo "🚀 Development environment ready!"
	@echo "📊 API: http://localhost:8000"
	@echo "📚 Docs: http://localhost:8000/docs"

prod: setup build up-prod ## Quick production setup
	@echo "🚀 Production environment ready!"
	@echo "📊 API: http://localhost:8000"
	@echo "📚 Docs: http://localhost:8000/docs"

# Information commands
info: ## Show application information
	@echo "Job Recommendation API Information"
	@echo "=================================="
	@echo "📊 API URL: http://localhost:8000"
	@echo "📚 Documentation: http://localhost:8000/docs"
	@echo "🔍 Health Check: http://localhost:8000/health"
	@echo "🐳 Docker Status:"
	@docker compose ps
