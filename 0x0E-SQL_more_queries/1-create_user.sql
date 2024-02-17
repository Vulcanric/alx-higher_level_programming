-- Create a new user having all privilege attached to it
CREATE USER IF NOT EXISTS 'user_0d_1'@'localhost' IDENTIFIED BY 'User_0d_1_pwd_@';
GRANT ALL PRIVILEGES ON *.* TO 'user_0d_1'@'localhost';
