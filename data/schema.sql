CREATE TABLE users
(
	id INTEGER PRIMARY KEY,
	username TEXT UNIQUE
);

CREATE TABLE transactions
(
	id INTEGER PRIMARY KEY,
	deposit INTEGER,
	user_id INTEGER REFERENCES users
);
