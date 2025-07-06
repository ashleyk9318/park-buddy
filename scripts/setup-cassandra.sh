#!/bin/bash

# Setup script for Cassandra development environment

set -e

echo "🚀 Setting up Cassandra for Park Buddy development..."

# Check if Docker is running
if ! docker info > /dev/null 2>&1; then
    echo "❌ Docker is not running. Please start Docker and try again."
    exit 1
fi

# Stop any existing containers
echo "🛑 Stopping any existing Cassandra containers..."
docker-compose down -v 2>/dev/null || true

# Start Cassandra
echo "📦 Starting Cassandra container..."
docker-compose up -d cassandra

# Wait for Cassandra to be ready
echo "⏳ Waiting for Cassandra to be ready..."
until docker-compose exec -T cassandra cqlsh -e "describe keyspaces" > /dev/null 2>&1; do
    echo "   Still waiting for Cassandra to start..."
    sleep 5
done

echo "✅ Cassandra is ready!"

# Show status
echo "📊 Cassandra Status:"
docker-compose ps

echo ""
echo "🔗 Cassandra is available at: localhost:9042"
echo "🗄️  Keyspace: store"
echo ""
echo "To stop Cassandra: docker-compose down"
echo "To view logs: docker-compose logs cassandra"
echo "To connect with cqlsh: docker-compose exec cassandra cqlsh" 