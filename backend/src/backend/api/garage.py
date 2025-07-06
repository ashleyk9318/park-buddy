from backend.database import get_session
from backend.database.schema import Garage

def get_garages() -> list[Garage]:
    """Get all garages in our database"""
    session = get_session()
    sql = "SELECT * FROM garages"
    garages = session.execute(sql)
    to_ret: list[Garage] = []
    for garage in garages:
        to_ret.append(Garage(garage.garage_id, garage.location, garage.last_update_timestamp))
    return to_ret

def get_garage_by_id(garage_id: str) -> Garage:
    """Get the garage by its id"""
    session = get_session()
    sql = "SELECT * FROM garages WHERE garage_id = %s"
    row = session.execute(sql, (garage_id,))
    return Garage(row.garage_id, row.location, row.last_update_timestamp)

def get_garage_by_location(garage_location: str) -> Garage:
    """Get the garage by its location"""
    session = get_session()
    sql = "SELECT * FROM garages WHERE location = %s"
    row = session.execute(sql, (garage_location,))
    return Garage(row.garage_id, row.location, row.last_update_timestamp)
