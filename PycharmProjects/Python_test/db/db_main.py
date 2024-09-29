import sqlite3
from db import queries


db = sqlite3.connect('db/products.sqlite3')
cursor = db.cursor()


async def sql_create():
    if db:
        print('База данных подключена!')
    cursor.execute(queries.CREATE_TABLE_PRODUCTS)
    db.commit()



async def sql_insert_products(name_product, category, size, price, product_id, photo):
    with sqlite3.connect('db/products.sqlite3') as db_with:
        cursor_with = db_with.cursor()
        cursor_with.execute(queries.INSERT_PRODUCTS_QUERY, (
        name_product,
        category,
        size,
        price,
        product_id,
        photo
    ))
    db.commit()
