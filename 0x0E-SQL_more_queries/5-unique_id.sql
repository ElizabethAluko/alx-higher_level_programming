--Create table unique_id with id that is unque and not empty.
CREATE TABLE IF NOT EXISTS unique_id(
	id int DEFAULT '1',
	name VARCHAR(256),
	UNIQUE(id)
	);
