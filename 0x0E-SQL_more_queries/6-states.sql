-- Create database and table with unique auto generated id that is primary key.
CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;
USE hbtn_0d_usa;
CREATE TABLE IF NOT EXISTS states(
	id INT AUTO INCREMENT NOT NULL,
	name VARCHAR(256) NOT NULL,
	UNIQUE (id),
	PRIMARY KEY (id)
	);
