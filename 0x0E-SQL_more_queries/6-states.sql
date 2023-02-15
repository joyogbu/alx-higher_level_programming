-- create a database and a table with auto generate id
USE hbtn_0d_usa;
CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;
CREATE TABLE IF NOT EXISTS states(id INT PRIMARY KEY AUTO_INCREMENT NOT NULL, name VARCHAR(256))
