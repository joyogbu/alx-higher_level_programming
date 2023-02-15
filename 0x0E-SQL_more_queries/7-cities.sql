-- create a database and a table with foreign key
CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;
USE hbtn_0d_usa;
CREATE TABLE IF NOT EXISTS cities(id INT PRIMARY KEY UNIQUE AUTO_INCREMENT NOT NULL, state_id INT FOREIGN KEY REFERENCES states(id) NOT NULL, name VARCHAR(256) NOT NULL)
