from backend.database import get_session
from backend.database.schema import ParkingSpot, SpotStatus

def get_parking_spots(floor_id: str) -> list[ParkingSpot]:
    session = get_session()
    query = "SELECT * FROM parking_spots WHERE floor_id = %s"
    parking_spots = session.execute(query, (floor_id,))
    to_ret: list[ParkingSpot] = []
    for parking_spot in parking_spots:
        to_ret.append(ParkingSpot(parking_spot.spot_id, parking_spot.floor_id, parking_spot.spot_number, parking_spot.status, parking_spot.last_update_timestamp))
    return to_ret

def get_parking_spot_by_id(spot_id: str) -> ParkingSpot:
    session = get_session()
    query = "SELECT * FROM parking_spots WHERE spot_id = %s"
    row = session.execute(query, (spot_id,))
    return ParkingSpot(row.spot_id, row.floor_id, row.spot_number, row.status, row.last_update_timestamp)

def get_parking_spot_by_spot_number(spot_number: str, floor_id: str) -> ParkingSpot:
    session = get_session()
    query = "SELECT * FROM parking_spots WHERE spot_number = %s AND floor_id = %s"
    row = session.execute(query, (spot_number, floor_id))
    return ParkingSpot(row.spot_id, row.floor_id, row.spot_number, row.status, row.last_update_timestamp)

def get_parking_spots_by_status(floor_id: str, status: SpotStatus) -> list[ParkingSpot]:
    session = get_session()
    query = "SELECT * From parking_spots WHERE floor_id = %s AND status = %s"
    parking_spots = session.execute(query, (floor_id, status))
    to_ret: list[ParkingSpot] = []
    for parking_spot in parking_spots:
        to_ret.append(ParkingSpot(parking_spot.spot_id, parking_spot.floor_id, parking_spot.spot_number, parking_spot.status, parking_spot.last_update_timestamp))
    return to_ret


