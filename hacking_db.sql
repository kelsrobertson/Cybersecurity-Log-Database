CREATE DATABASE hacking_db;
USE hacking_db;

CREATE TABLE Users (
	user_id INT PRIMARY KEY,
	username VARCHAR (100),
	password VARCHAR (100)
);

INSERT INTO Users (user_id, username, password) VALUES
(1, 'zappyapple', 'pineapple'), (2, 'princesskitty', 'meowmeow'), (3, 'rededition', 'redbull');


CREATE TABLE Dummy (
	name VARCHAR (100),
	value INT,
	dob DATE,
	age INT,
	email VARCHAR (100)
);

INSERT INTO Dummy (name, value, dob, age, email) VALUES
( 'Lucas', 234, '1999-10-29', 25, 'Lucas.C@gmail.com'),
( 'Sam', 567, '1998-12-02', 25, 'SAmmy.Dad@gmail.com'),
( 'Dodge',457, '2000-01-12', 24, 'ramboy@gmail.com');



