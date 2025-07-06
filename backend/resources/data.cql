-- Create a keyspace
CREATE KEYSPACE IF NOT EXISTS store WITH REPLICATION = { 'class' : 'SimpleStrategy', 'replication_factor' : '1' };

-- Create a table
CREATE TABLE IF NOT EXISTS store.garages (
    garage_id text PRIMARY KEY,
    location text,
    last_update_timestamp timestamp
);

CREATE TABLE IF NOT EXISTS store.floors (
    floor_id text PRIMARY KEY,
    garage_id text,
    floor_number text,
    last_update_timestamp timestamp
);

CREATE TABLE IF NOT EXISTS store.parking_spots (
    spot_id text PRIMARY KEY,
    floor_id text,
    spot_number text,
    status text,
    last_update_timestamp timestamp
);

-- Insert some data
INSERT INTO store.shopping_cart
(userid, item_count, last_update_timestamp)
VALUES ('9876', 2, toTimeStamp(now()));
INSERT INTO store.shopping_cart
(userid, item_count, last_update_timestamp)
VALUES ('1234', 5, toTimeStamp(now()));