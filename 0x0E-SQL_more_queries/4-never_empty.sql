-- Creates the table 'id_not_null' if it doesn't exist with columns:
-- 'id' & 'name'
CREATE TABLE IF NOT EXISTS id_not_null (
    id   INT  DEFAULT 1,
    name VARCHAR(256)
);
