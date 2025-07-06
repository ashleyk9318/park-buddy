-- Create a keyspace for the parking garage application
CREATE KEYSPACE IF NOT EXISTS store 
WITH REPLICATION = { 'class' : 'SimpleStrategy', 'replication_factor' : '1' };

-- Use the keyspace
USE store;

-- Create garages table
CREATE TABLE IF NOT EXISTS garages (
    garage_id text PRIMARY KEY,
    location text,
    last_update_timestamp timestamp
);

-- Create floors table with garage_id as clustering key
CREATE TABLE IF NOT EXISTS floors (
    garage_id text,
    floor_id text,
    floor_number text,
    last_update_timestamp timestamp,
    PRIMARY KEY (garage_id, floor_id)
);

-- Create parking_spots table with floor_id as clustering key
CREATE TABLE IF NOT EXISTS parking_spots (
    floor_id text,
    spot_id text,
    spot_number text,
    status text,
    last_update_timestamp timestamp,
    PRIMARY KEY (floor_id, spot_id)
);

-- Create secondary indexes for additional query patterns
CREATE INDEX IF NOT EXISTS ON floors (floor_id);
CREATE INDEX IF NOT EXISTS ON parking_spots (spot_id);
CREATE INDEX IF NOT EXISTS ON parking_spots (status);

-- Insert sample garage data
INSERT INTO garages (garage_id, location, last_update_timestamp) 
VALUES ('garage_001', 'Downtown Central', toTimestamp(now()));

INSERT INTO garages (garage_id, location, last_update_timestamp) 
VALUES ('garage_002', 'Shopping Mall West', toTimestamp(now()));

-- Insert sample floor data
INSERT INTO floors (garage_id, floor_id, floor_number, last_update_timestamp) 
VALUES ('garage_001', 'floor_001', '1', toTimestamp(now()));

INSERT INTO floors (garage_id, floor_id, floor_number, last_update_timestamp) 
VALUES ('garage_001', 'floor_002', '2', toTimestamp(now()));

INSERT INTO floors (garage_id, floor_id, floor_number, last_update_timestamp) 
VALUES ('garage_002', 'floor_003', '1', toTimestamp(now()));

-- Insert sample parking spot data
INSERT INTO parking_spots (floor_id, spot_id, spot_number, status, last_update_timestamp) 
VALUES ('floor_001', 'spot_001', 'A1', 'available', toTimestamp(now()));

INSERT INTO parking_spots (floor_id, spot_id, spot_number, status, last_update_timestamp) 
VALUES ('floor_001', 'spot_002', 'A2', 'occupied', toTimestamp(now()));

INSERT INTO parking_spots (floor_id, spot_id, spot_number, status, last_update_timestamp) 
VALUES ('floor_001', 'spot_003', 'A3', 'available', toTimestamp(now()));

INSERT INTO parking_spots (floor_id, spot_id, spot_number, status, last_update_timestamp) 
VALUES ('floor_002', 'spot_004', 'B1', 'available', toTimestamp(now()));

INSERT INTO parking_spots (floor_id, spot_id, spot_number, status, last_update_timestamp) 
VALUES ('floor_003', 'spot_005', 'C1', 'occupied', toTimestamp(now())); 