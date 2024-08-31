CREATE TABLE categories (
    id SERIAL PRIMARY KEY,
    name VARCHAR(100) NOT NULL
);

CREATE TABLE products (
    id SERIAL PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    description TEXT,
    price NUMERIC(10, 2),
    category_id INTEGER REFERENCES categories(id)
);

CREATE TABLE reviews (
    id SERIAL PRIMARY KEY,
    content TEXT,
    rating INTEGER CHECK(rating >= 1 AND rating <= 5),
    product_id INTEGER REFERENCES products(id)
);


INSERT INTO categories (name) VALUES
('Electronics'),
('Books'),
('Clothing'),
('Home & Kitchen'),
('Toys & Games');


INSERT INTO products (name, description, price, category_id) VALUES
('Smartphone', 'A high-end smartphone with a sleek design.', 699.99, 1),
('Laptop', 'A powerful laptop for professionals.', 1199.99, 1),
('Novel', 'A thrilling mystery novel.', 15.99, 2),
('T-Shirt', 'A comfortable cotton t-shirt.', 9.99, 3),
('Coffee Maker', 'An efficient coffee maker with multiple settings.', 49.99, 4),
('Board Game', 'A fun family board game for all ages.', 29.99, 5);


INSERT INTO reviews (content, rating, product_id) VALUES
('Excellent smartphone with great features!', 5, 1),
('Battery life could be better.', 3, 1),
('The laptop is fast and reliable.', 4, 2),
('Loved the storyline of this novel.', 5, 3),
('The shirt is comfortable and fits well.', 4, 4),
('Makes great coffee quickly.', 5, 5),
('The board game is entertaining and fun.', 4, 6),
('Not as fun as expected.', 3, 6);

select * from products;
select * from categories;
select * from reviews;


1. Retrieve All Products in a Specific Category
SELECT 
    p.id,
    p.name AS product_name,
    p.description,
    p.price,
    c.name AS category_name
FROM 
    products p
JOIN 
    categories c ON p.category_id = c.id
WHERE 
    c.name = 'Electronics';

2. Retrieve Products with a Name Matching a Search Term
SELECT 
    p.id,
    p.name AS product_name,
    p.description,
    p.price,
    c.name AS category_name
FROM 
    products p
JOIN 
    categories c ON p.category_id = c.id
WHERE 
    p.name ILIKE '%Laptop%';

3. Retrieve Products with a Description Matching a Search Term
SELECT 
    p.id,
    p.name AS product_name,
    p.description,
    p.price,
    c.name AS category_name
FROM 
    products p
JOIN 
    categories c ON p.category_id = c.id
WHERE 
    p.description ILIKE '%sleek%';

4. Retrieve Products in a Specific Category with a Search Term in Name or Description
SELECT 
    p.id,
    p.name AS product_name,
    p.description,
    p.price,
    c.name AS category_name
FROM 
    products p
JOIN 
    categories c ON p.category_id = c.id
WHERE 
    c.name = 'Books'
    AND (p.name ILIKE '%thrilling%' OR p.description ILIKE '%thrilling%');


