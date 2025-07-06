from backend.database import get_session
from backend.database.schema import Floor

def get_floors(garage_id: str) -> list[Floor]:
    session = get_session()
    query = "SELECT * FROM floors WHERE garage_id = %s"
    floors = session.execute(query, (garage_id,))
    to_ret: list[Floor] = []
    for floor in floors:
        to_ret.append(Floor(floor.floor_id, floor.garage_id, floor.floor_number, floor.last_update_timestamp))
    return to_ret

def get_floor_by_id(floor_id: str) -> Floor:
    session = get_session()
    query = "SELECT * FROM floors WHERE floor_id = %s"
    row = session.execute(query, (floor_id,))
    return Floor(row.floor_id, row.garage_id, row.floor_number, row.last_update_timestamp)

def get_floor_by_floor_number(floor_number: str, garage_id: str) -> Floor:
    session = get_session()
    query = "SELECT * FROM floors WHERE floor_number = %s AND garage_id = %s"
    row = session.execute(query, (floor_number, garage_id))
    return Floor(row.floor_id, row.garage_id, row.floor_number, row.last_update_timestamp)