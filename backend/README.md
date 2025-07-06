# Park Buddy Backend

A Flask-based REST API for managing parking garage data using Cassandra as the database.

## Setup

### Prerequisites
- Python 3.9+
- Poetry (for dependency management)
- Docker (for running Cassandra)

### Installation

1. Install dependencies:
```bash
poetry install
```

2. Start Cassandra (using Docker):
```bash
# From the project root
./scripts/setup-cassandra.sh
```

Or manually:
```bash
docker-compose up -d cassandra
```

3. Run the application:
```bash
poetry run python src/backend/server.py
```

## API Endpoints

### Garages
- `GET /api/garages` - Get all garages
- `GET /api/garages/<garage_id>` - Get garage by ID
- `GET /api/garages/location/<location>` - Get garage by location

### Floors
- `GET /api/garages/<garage_id>/floors` - Get floors for a garage
- `GET /api/floors/<floor_id>` - Get floor by ID
- `GET /api/garages/<garage_id>/floors/<floor_number>` - Get floor by number

### Parking Spots
- `GET /api/floors/<floor_id>/parking-spots` - Get parking spots for a floor
- `GET /api/parking-spots/<spot_id>` - Get parking spot by ID
- `GET /api/floors/<floor_id>/parking-spots/<spot_number>` - Get parking spot by number
- `GET /api/floors/<floor_id>/parking-spots/status/<status>` - Get parking spots by status

## Testing

Run tests without Cassandra:
```bash
poetry run pytest tests/ -m "not cassandra"
```

Run all tests (requires Cassandra):
```bash
poetry run pytest tests/
```

## Development

The application uses a lazy connection pattern for Cassandra, so it will only connect when needed. This allows for development and testing without requiring Cassandra to be running.

### Database Schema

The database includes three main tables:
- `garages` - Stores garage information
- `floors` - Stores floor information for each garage
- `parking_spots` - Stores parking spot information for each floor

Sample data is automatically inserted when Cassandra starts up.
