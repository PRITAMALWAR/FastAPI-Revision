from fastapi import FastAPI

app = FastAPI()


# ============================================================
# 1. HOME
# ============================================================

@app.get("/")
def home():
    return {
        "message": "Welcome to Lesson 2 - Path & Query Parameters"
    }


# ============================================================
# 2. PATH PARAMETER
# ============================================================
# Example:
# GET /products/5
#
# 5 is the product_id
# ============================================================

@app.get("/products/{product_id}")
def get_product(product_id: int):
    return {
        "message": "Product found",
        "product_id": product_id
    }


# ============================================================
# 3. PATH PARAMETER - PRODUCT DETAILS
# ============================================================
# Example:
# GET /products/10/details
# ============================================================

@app.get("/products/{product_id}/details")
def product_details(product_id: int):
    return {
        "product_id": product_id,
        "title": "Nike Air Max",
        "category": "Shoes",
        "price": 4999
    }


# ============================================================
# 4. MULTIPLE PATH PARAMETERS
# ============================================================
# Example:
# GET /users/5/products/10
# ============================================================

@app.get("/users/{user_id}/products/{product_id}")
def user_product(user_id: int, product_id: int):
    return {
        "user_id": user_id,
        "product_id": product_id
    }


# ============================================================
# 5. QUERY PARAMETER
# ============================================================
# Example:
# GET /search?name=Nike
# ============================================================

@app.get("/search")
def search(name: str):
    return {
        "search_name": name
    }


# ============================================================
# 6. MULTIPLE QUERY PARAMETERS
# ============================================================
# Example:
# GET /filter?category=Shoes&price=5000
# ============================================================

@app.get("/filter")
def filter_products(category: str, price: int):
    return {
        "category": category,
        "max_price": price
    }


# ============================================================
# 7. OPTIONAL QUERY PARAMETER
# ============================================================
# Example:
#
# /products-search
#
# OR
#
# /products-search?name=Nike
# ============================================================

@app.get("/products-search")
def products_search(name: str | None = None):
    return {
        "name": name
    }


# ============================================================
# 8. OPTIONAL MULTIPLE QUERY PARAMETERS
# ============================================================
# Examples:
#
# /products-filter
#
# /products-filter?category=Shoes
#
# /products-filter?category=Shoes&max_price=5000
# ============================================================

@app.get("/products-filter")
def products_filter(
    category: str | None = None,
    max_price: int | None = None
):
    return {
        "category": category,
        "max_price": max_price
    }


# ============================================================
# 9. QUERY PARAMETER WITH DEFAULT VALUE
# ============================================================
# Example:
#
# /products-page
#
# Default page = 1
#
# /products-page?page=2
# ============================================================

@app.get("/products-page")
def products_page(page: int = 1):
    return {
        "page": page
    }


# ============================================================
# 10. QUERY PARAMETERS WITH DEFAULT VALUES
# ============================================================
# Example:
#
# /products-list
#
# /products-list?page=2&limit=20
# ============================================================

@app.get("/products-list")
def products_list(
    page: int = 1,
    limit: int = 10
):
    return {
        "page": page,
        "limit": limit
    }