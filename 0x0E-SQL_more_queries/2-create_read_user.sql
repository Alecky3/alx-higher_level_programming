-- Creates the database 'hbtn_0d_2' and the 'user user_0d_2' if they doesn't exist
-- The user_0d_2 should have SELECT privilege on 'hbtn_0d_2'
CREATE DATABASE IF NOT EXISTS hbtn_0d_2;
CREATE USER IF NOT EXISTS 'user_0d_2'@'localhost' IDENTIFIED BY 'user_0d_2_pwd';
GRANT SELECT ON hbtn_0d_2.* TO 'user_0d_2'@'localhost';
