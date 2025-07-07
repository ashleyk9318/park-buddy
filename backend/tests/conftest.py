import pytest
from unittest.mock import Mock, patch
from datetime import datetime
from backend.database.schema import SpotStatus, ParkingSpot

# Mock data for testing
MOCK_PARKING_SPOTS = [
    ParkingSpot("spot1", "floor1", "A1", SpotStatus.AVAILABLE, datetime.now()),
    ParkingSpot("spot2", "floor1", "A2", SpotStatus.OCCUPIED, datetime.now()),
    ParkingSpot("spot3", "floor1", "A3", SpotStatus.AVAILABLE, datetime.now()),
    ParkingSpot("spot4", "floor2", "B1", SpotStatus.AVAILABLE, datetime.now()),
    ParkingSpot("spot5", "floor2", "B2", SpotStatus.OCCUPIED, datetime.now()),
]

@pytest.fixture(scope="session")
def mock_cassandra_session():
    """Create a mock Cassandra session that can be shared across tests"""
    mock_session = Mock()
    
    def mock_execute(query, params=None):
        mock_result = Mock()
        
        # Ensure params is a tuple/list for indexing
        if params is None:
            params = ()
        
        if "SELECT * FROM parking_spots WHERE floor_id" in query and len(params) > 0:
            # Return all spots for a floor
            mock_result.__iter__ = lambda self: iter([
                Mock(
                    spot_id=spot.spot_id,
                    floor_id=spot.floor_id,
                    spot_number=spot.spot_number,
                    status=spot.status,
                    last_update_timestamp=spot.last_update_timestamp
                ) for spot in MOCK_PARKING_SPOTS if spot.floor_id == params[0]
            ])
        elif "SELECT * FROM parking_spots WHERE spot_id" in query and len(params) > 0:
            # Return specific spot by ID
            spot = next((s for s in MOCK_PARKING_SPOTS if s.spot_id == params[0]), None)
            if spot:
                mock_result = Mock(
                    spot_id=spot.spot_id,
                    floor_id=spot.floor_id,
                    spot_number=spot.spot_number,
                    status=spot.status,
                    last_update_timestamp=spot.last_update_timestamp
                )
        elif "SELECT * FROM parking_spots WHERE spot_number" in query and len(params) > 1:
            # Return specific spot by spot number and floor
            spot = next((s for s in MOCK_PARKING_SPOTS if s.spot_number == params[0] and s.floor_id == params[1]), None)
            if spot:
                mock_result = Mock(
                    spot_id=spot.spot_id,
                    floor_id=spot.floor_id,
                    spot_number=spot.spot_number,
                    status=spot.status,
                    last_update_timestamp=spot.last_update_timestamp
                )
        elif "SELECT * From parking_spots WHERE floor_id" in query and "status" in query and len(params) > 1:
            # Return spots by status
            mock_result.__iter__ = lambda self: iter([
                Mock(
                    spot_id=spot.spot_id,
                    floor_id=spot.floor_id,
                    spot_number=spot.spot_number,
                    status=spot.status,
                    last_update_timestamp=spot.last_update_timestamp
                ) for spot in MOCK_PARKING_SPOTS if spot.floor_id == params[0] and spot.status == params[1]
            ])
        
        return mock_result
    
    # Create a proper Mock for the execute method so we can track calls
    mock_execute_mock = Mock(side_effect=mock_execute)
    mock_session.execute = mock_execute_mock
    return mock_session

@pytest.fixture
def mock_database(mock_cassandra_session):
    """Mock the database session for all database operations"""
    with patch('backend.database.client.get_session', return_value=mock_cassandra_session):
        with patch('backend.api.parking_spots.get_session', return_value=mock_cassandra_session):
            yield mock_cassandra_session

@pytest.fixture
def sample_parking_spots():
    """Provide sample parking spot data for tests"""
    return MOCK_PARKING_SPOTS.copy() 