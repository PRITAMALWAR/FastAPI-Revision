from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import sqlite3

app = FastAPI()


# ============================================================
# DATABASE CONNECTION
# ============================================================

DATABASE = "products.db"


def get_db_connection():
    connection = sqlite3.connect(DATABASE)

    connection.row_factory = sqlite3.Row

    return connection


# ============================================================
# CREATE DATABASE TABLE
# ============================================================

def create_table():

    connection = get_db_connection()

    connection.execute("""
        CREATE TABLE IF NOT EXISTS products (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            title TEXT NOT NULL,
            category TEXT NOT NULL,
            price INTEGER NOT NULL,
            size TEXT NOT NULL
        )
    """)

    connection.commit()
    connection.close()


create_table()


# ============================================================
# PYDANTIC MODEL
# ============================================================

class Product(BaseModel):
    title: str
    category: str
    price: int
    size: str


# ============================================================
# HOME
# ============================================================

@app.get("/")
def home():

    return {
        "message": "Lesson 6 - SQLite Database"
    }


# ============================================================
# CREATE PRODUCT
# POST /products
# ============================================================

@app.post("/products")
def create_product(product: Product):

    connection = get_db_connection()

    cursor = connection.execute("""
        INSERT INTO products
        (title, category, price, size)
        VALUES (?, ?, ?, ?)
    """, (
        product.title,
        product.category,
        product.price,
        product.size
    ))

    connection.commit()

    product_id = cursor.lastrowid

    connection.close()

    return {
        "message": "Product created successfully",
        "product_id": product_id,
        "product": product.model_dump()
    }


# ============================================================
# READ ALL PRODUCTS
# GET /products
# ============================================================

@app.get("/products")
def get_products():

    connection = get_db_connection()

    products = connection.execute("""
        SELECT *
        FROM products
    """).fetchall()

    connection.close()

    return {
        "count": len(products),
        "products": [dict(product) for product in products]
    }


# ============================================================
# READ ONE PRODUCT
# GET /products/{product_id}
# ============================================================

@app.get("/products/{product_id}")
def get_product(product_id: int):

    connection = get_db_connection()

    product = connection.execute("""
        SELECT *
        FROM products
        WHERE id = ?
    """, (product_id,)).fetchone()

    connection.close()

    if product is None:

        raise HTTPException(
            status_code=404,
            detail="Product not found"
        )

    return dict(product)


# ============================================================
# UPDATE PRODUCT
# PUT /products/{product_id}
# ============================================================

@app.put("/products/{product_id}")
def update_product(
    product_id: int,
    product: Product
):

    connection = get_db_connection()

    existing_product = connection.execute("""
        SELECT *
        FROM products
        WHERE id = ?
    """, (product_id,)).fetchone()

    if existing_product is None:

        connection.close()

        raise HTTPException(
            status_code=404,
            detail="Product not found"
        )

    connection.execute("""
        UPDATE products
        SET
            title = ?,
            category = ?,
            price = ?,
            size = ?
        WHERE id = ?
    """, (
        product.title,
        product.category,
        product.price,
        product.size,
        product_id
    ))

    connection.commit()
    connection.close()

    return {
        "message": "Product updated successfully",
        "product_id": product_id,
        "product": product.model_dump()
    }


# ============================================================
# DELETE PRODUCT
# DELETE /products/{product_id}
# ============================================================

@app.delete("/products/{product_id}")
def delete_product(product_id: int):

    connection = get_db_connection()

    existing_product = connection.execute("""
        SELECT *
        FROM products
        WHERE id = ?
    """, (product_id,)).fetchone()

    if existing_product is None:

        connection.close()

        raise HTTPException(
            status_code=404,
            detail="Product not found"
        )

    connection.execute("""
        DELETE FROM products
        WHERE id = ?
    """, (product_id,))

    connection.commit()
    connection.close()

    return {
        "message": "Product deleted successfully",
        "product_id": product_id
    }