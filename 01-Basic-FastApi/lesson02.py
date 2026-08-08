from fastapi import FastAPI

app = FastAPI()

# -----------------------------
# Sample Product Data (JSON)
# -----------------------------
products = [
    {
        "id": 1,
        "title": "Nike Air Max",
        "category": "Shoes",
        "price": 4999,
        "size": 9
    },
    {
        "id": 2,
        "title": "Adidas Ultraboost",
        "category": "Shoes",
        "price": 6999,
        "size": 10
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
        "size": 32
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

# --------------------------------
# Home
# --------------------------------
@app.get("/")
def home():
    return {
        "message": "Welcome to FastAPI Course"
    }


# --------------------------------
# Get All Products
# --------------------------------
@app.get("/products")
def get_products():
    return products


# --------------------------------
# Get Product by ID (Path Parameter)
# --------------------------------
@app.get("/products/{product_id}")
def get_product(product_id: int):

    for product in products:
        if product["id"] == product_id:
            return product

    return {
        "message": "Product Not Found"
    }


# --------------------------------
# Search by Category (Query Parameter)
# Example:
# /search?category=Shoes
# --------------------------------
@app.get("/search")
def search_product(category: str):

    result = []

    for product in products:
        if product["category"].lower() == category.lower():
            result.append(product)

    return result


# --------------------------------
# Filter by Maximum Price
# Example:
# /price?max_price=5000
# --------------------------------
@app.get("/price")
def filter_price(max_price: int):

    result = []

    for product in products:
        if product["price"] <= max_price:
            result.append(product)

    return result


# --------------------------------
# Get All Categories
# --------------------------------
@app.get("/categories")
def get_categories():

    categories = []

    for product in products:
        if product["category"] not in categories:
            categories.append(product["category"])

    return categories


# --------------------------------
# Electronics Products
# --------------------------------
@app.get("/electronics")
def electronics():

    result = []

    for product in products:
        if product["category"] == "Electronics":
            result.append(product)

    return result


# --------------------------------
# Expensive Products
# Example:
# /expensive?price=10000
# --------------------------------
@app.get("/expensive")
def expensive(price: int):

    result = []

    for product in products:
        if product["price"] > price:
            result.append(product)

    return result