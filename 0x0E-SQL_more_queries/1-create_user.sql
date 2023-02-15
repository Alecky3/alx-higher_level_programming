-- Creates the MySQL  user 'user_0d_1'.
-- 'user_0d_1' should have all privileges on the MySQL server
-- 'user_0d_1' passowrd should be set to 'user_0d_1_pwd'
-- if user exists, do nothing
CREATE USER IF NOT EXISTS 'user_0d_1'@'localhost' IDENTIFIED BY 'user_0d_1_pwd';
GRANT ALL PRIVILEGES ON *.* TO 'user_0d_1'@'localhost'
