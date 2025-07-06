from enum import Enum


class Garage:
    def __init__(self, garage_id: str, location: str, last_update_timestamp):
        self.garage_id = garage_id
        self.location = location
        self.last_update_timestamp = last_update_timestamp

class Floor:
    def __init__(self, floor_id: str, garage_id: str, floor_number: str, last_update_timestamp):
        self.floor_id = floor_id
        self.garage_id = garage_id
        self.floor_number = floor_number
        self.last_update_timestamp = last_update_timestamp

class SpotStatus(Enum):
    UNKNOWN = "unknown"
    AVAILABLE = "available"
    OCCUPIED = "occupied"

class ParkingSpot:
    def __init__(self, spot_id: str, floor_id: str, spot_number: str, status: SpotStatus, last_update_timestamp):
        self.spot_id = spot_id
        self.floor_id = floor_id
        self.spot_number = spot_number
        self.status = status
        self.last_update_timestamp = last_update_timestamp