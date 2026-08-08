from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()


# ==========================================
# PRODUCT MODEL
# ==========================================

class Product(BaseModel):
    title: str
    category: str
    price: int
    size: str


# ==========================================
# PRODUCT DATA
# ==========================================

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
    },
    {
        "id": 4,
        "title": "Levi's Jeans",
        "category": "Clothing",
        "price": 2499,
        "size": "32"
    },
    {
        "id": 5,
        "title": "Apple Watch",
        "category": "Electronics",
        "price": 29999,
        "size": "44mm"
    },
    {
        "id": 6,
        "title": "Samsung Galaxy Buds",
        "category": "Electronics",
        "price": 7999,
        "size": "One Size"
    },
    {
        "id": 7,
        "title": "Wildcraft Backpack",
        "category": "Bags",
        "price": 1899,
        "size": "25L"
    },
    {
        "id": 8,
        "title": "HP Laptop",
        "category": "Electronics",
        "price": 58999,
        "size": "15.6 inch"
    },
    {
        "id": 9,
        "title": "Boat Headphones",
        "category": "Electronics",
        "price": 1499,
        "size": "Standard"
    },
    {
        "id": 10,
        "title": "Casio Watch",
        "category": "Accessories",
        "price": 3499,
        "size": "Free Size"
    }
]


# ==========================================
# HOME
# ==========================================

@app.get("/")
def home():
    return {
        "message": "Welcome to FastAPI"
    }


# ==========================================
# GET ALL PRODUCTS
# ==========================================

@app.get("/products")
def get_products():
    return products


# ==========================================
# GET ONE PRODUCT
# ==========================================

@app.get("/products/{product_id}")
def get_product(product_id: int):

    for product in products:

        if product["id"] == product_id:
            return product

    return {
        "message": "Product not found"
    }


# ==========================================
# CREATE PRODUCT
# POST /products
# ==========================================

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


# ==========================================
# SEARCH BY CATEGORY
# ==========================================

@app.get("/search")
def search_product(category: str):

    result = []

    for product in products:

        if product["category"].lower() == category.lower():
            result.append(product)

    return result


# ==========================================
# FILTER BY PRICE
# ==========================================

@app.get("/price")
def filter_price(max_price: int):

    result = []

    for product in products:

        if product["price"] <= max_price:
            result.append(product)

    return result


# ==========================================
# GET CATEGORIES
# ==========================================

@app.get("/categories")
def get_categories():

    categories = []

    for product in products:

        if product["category"] not in categories:
            categories.append(product["category"])

    return categories


# ==========================================
# ELECTRONICS PRODUCTS
# ==========================================

@app.get("/electronics")
def electronics():

    result = []

    for product in products:

        if product["category"] == "Electronics":
            result.append(product)

    return result


# ==========================================
# EXPENSIVE PRODUCTS
# ==========================================

@app.get("/expensive")
def expensive(price: int):

    result = []

    for product in products:

        if product["price"] > price:
            result.append(product)

    return result