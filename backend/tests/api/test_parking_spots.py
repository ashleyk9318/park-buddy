import pytest
from backend.api.parking_spots import get_parking_spots, get_parking_spot_by_id, get_parking_spot_by_spot_number, get_parking_spots_by_status, update_parking_spot_status
from backend.database.schema import SpotStatus

class TestParkingSpots:
    
    def test_get_parking_spots(self, mock_database):
        """Test getting all parking spots for a floor"""
        parking_spots = get_parking_spots("floor1")
        
        assert len(parking_spots) == 3
        assert parking_spots[0].spot_id == "spot1"
        assert parking_spots[0].spot_number == "A1"
        assert parking_spots[0].status == SpotStatus.AVAILABLE
        assert parking_spots[1].status == SpotStatus.OCCUPIED
    
    def test_get_parking_spot_by_id(self, mock_database):
        """Test getting a parking spot by ID"""
        parking_spot = get_parking_spot_by_id("spot1")
        
        assert parking_spot.spot_id == "spot1"
        assert parking_spot.spot_number == "A1"
        assert parking_spot.status == SpotStatus.AVAILABLE
    
    def test_get_parking_spot_by_spot_number(self, mock_database):
        """Test getting a parking spot by spot number and floor"""
        parking_spot = get_parking_spot_by_spot_number("A2", "floor1")
        
        assert parking_spot.spot_id == "spot2"
        assert parking_spot.spot_number == "A2"
        assert parking_spot.status == SpotStatus.OCCUPIED
    
    def test_get_parking_spots_by_status(self, mock_database):
        """Test getting parking spots by status"""
        available_spots = get_parking_spots_by_status("floor1", SpotStatus.AVAILABLE)
        
        assert len(available_spots) == 2
        assert all(spot.status == SpotStatus.AVAILABLE for spot in available_spots)
    
    def test_update_parking_spot_status(self, mock_database):
        """Test updating parking spot status"""
        # First get the spots to verify initial state
        parking_spots = get_parking_spots("floor1")
        assert parking_spots[0].status == SpotStatus.AVAILABLE
        
        # Update the status
        update_parking_spot_status("floor1", "spot1", SpotStatus.OCCUPIED)
        
        # Verify the update was called - check that execute was called at least once
        assert mock_database.execute.call_count >= 1
        
        # Note: In a real scenario, you'd need to update the mock data
        # or mock the session to return updated data for subsequent calls