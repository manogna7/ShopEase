CREATE TABLE reviews (
	id SERIAL PRIMARY KEY,
	product_id INTEGER NOT NULL REFERENCES products(id) ON DELETE CASCADE,
	rating INTEGER NOT NULL,
	comment TEXT
);

SELECT * FROM categories