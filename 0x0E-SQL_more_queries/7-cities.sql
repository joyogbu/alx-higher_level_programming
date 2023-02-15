-- create a database and a table with foreign key
CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;
USE hbtn_0d_usa;
CREATE TABLE IF NOT EXISTS cities(id INT PRIMARY KEY UNIQUE AUTO_INCREMENT NOT NULL, state_id INT NOT NULL, nane VARCHAR(256) NOT NULL, FOREIGN KEY(state_id) REFERENCES states(id))
