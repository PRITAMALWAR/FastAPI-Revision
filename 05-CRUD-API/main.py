from fastapi import FastAPI, HTTPException
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
# TEMPORARY DATABASE
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
        "message": "Lesson 5 - CRUD API"
    }


# ============================================================
# CREATE
# POST /products
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


# ============================================================
# READ ALL
# GET /products
# ============================================================

@app.get("/products")
def get_products():

    return {
        "count": len(products),
        "products": products
    }


# ============================================================
# READ ONE
# GET /products/{product_id}
# ============================================================

@app.get("/products/{product_id}")
def get_product(product_id: int):

    for product in products:

        if product["id"] == product_id:
            return product

    raise HTTPException(
        status_code=404,
        detail="Product not found"
    )


# ============================================================
# UPDATE
# PUT /products/{product_id}
# ============================================================

@app.put("/products/{product_id}")
def update_product(
    product_id: int,
    product: Product
):

    for index, existing_product in enumerate(products):

        if existing_product["id"] == product_id:

            updated_product = {
                "id": product_id,
                "title": product.title,
                "category": product.category,
                "price": product.price,
                "size": product.size
            }

            products[index] = updated_product

            return {
                "message": "Product updated successfully",
                "product": updated_product
            }

    raise HTTPException(
        status_code=404,
        detail="Product not found"
    )


# ============================================================
# DELETE
# DELETE /products/{product_id}
# ============================================================

@app.delete("/products/{product_id}")
def delete_product(product_id: int):

    for index, product in enumerate(products):

        if product["id"] == product_id:

            deleted_product = products.pop(index)

            return {
                "message": "Product deleted successfully",
                "product": deleted_product
            }

    raise HTTPException(
        status_code=404,
        detail="Product not found"
    )