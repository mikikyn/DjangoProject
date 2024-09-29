CREATE_TABLE_PRODUCTS = """
    CREATE TABLE IF NOT EXISTS products (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name_product TEXT,
    category TEXT,
    size TEXT,
    price TEXT,
    product_id TEXT UNIQUE,
    photo TEXT
    )
"""

INSERT_PRODUCTS_QUERY = """
    INSERT INTO products (name_product, category, size, price, product_id, photo)
    VALUES (?, ?, ?, ?, ?, ?)
"""

GET_ALL_PRODUCTS_QUERY = """
    SELECT * FROM products
"""