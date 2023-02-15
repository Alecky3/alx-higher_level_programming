-- Creates the table 'unique_id' if it doesn't exist with columns:
-- 'id' & 'name'
CREATE TABLE IF NOT EXISTS unique_id (
    id   INT   DEFAULT 1 UNIQUE,
    name VARCHAR(256)
);
