from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()


# ============================================================
# PRODUCT MODEL
# ============================================================

class Product(BaseModel):
    title: str
    category: str
    price: int
    size: str


# ============================================================
# PRODUCT DATA
# ============================================================

products = [
    {
        "id": 1,
        "title": "Nike Air Max",
        "category": "Shoes",
        "price": 4999,
        "size": "9"
    },
    {
        "id": 2,
        "title": "Adidas Ultraboost",
        "category": "Shoes",
        "price": 6999,
        "size": "10"
    },
    {
        "id": 3,
        "title": "Puma T-Shirt",
        "category": "Clothing",
        "price": 999,
        "size": "M"
    }
]


# ============================================================
# HOME
# ============================================================

@app.get("/")
def home():
    return {
        "message": "Lesson 3 - POST + JSON"
    }


# ============================================================
# GET ALL PRODUCTS
# ============================================================

@app.get("/products")
def get_products():
    return products


# ============================================================
# GET ONE PRODUCT
# ============================================================

@app.get("/products/{product_id}")
def get_product(product_id: int):

    for product in products:

        if product["id"] == product_id:
            return product

    return {
        "message": "Product not found"
    }


# ============================================================
# POST - CREATE PRODUCT
# ============================================================

@app.post("/products")
def create_product(product: Product):

    new_product = {
        "id": len(products) + 1,
        "title": product.title,
        "category": product.category,
        "price": product.price,
        "size": product.size
    }

    products.append(new_product)

    return {
        "message": "Product created successfully",
        "product": new_product
    }