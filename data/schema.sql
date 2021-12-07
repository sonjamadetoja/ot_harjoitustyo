CREATE TABLE users
(
	id INTEGER PRIMARY KEY,
	username TEXT UNIQUE
);

CREATE TABLE transactions
(
	id INTEGER PRIMARY KEY,
	date TIMESTAMP,
	deposit INTEGER,
	user_id INTEGER REFERENCES users
	title TEXT, 
	category TEXT
);

CREATE TABLE test_users 
(
    id INTEGER PRIMARY KEY, 
    username TEXT UNIQUE
);

CREATE TABLE test_transactions 
(
    id INTEGER PRIMARY KEY, 
    date TIMESTAMP, 
    deposits INTEGER, 
    user_id INTEGER REFERENCES users, 
    title TEXT, 
    category TEXT
);
