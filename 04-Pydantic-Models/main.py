from fastapi import FastAPI
from pydantic import BaseModel, Field

app = FastAPI()


# ============================================================
# 1. BASIC PRODUCT MODEL
# ============================================================

class Product(BaseModel):
    title: str
    category: str
    price: int
    size: str


# ============================================================
# 2. PRODUCT MODEL WITH VALIDATION
# ============================================================

class ProductValidated(BaseModel):
    title: str = Field(min_length=3, max_length=50)
    category: str
    price: int = Field(gt=0, le=100000)
    size: str


# ============================================================
# 3. HOME
# ============================================================

@app.get("/")
def home():
    return {
        "message": "Lesson 4 - Pydantic Validation"
    }


# ============================================================
# 4. BASIC PYDANTIC MODEL
# ============================================================

@app.post("/products")
def create_product(product: Product):
    return {
        "message": "Product received successfully",
        "product": product
    }


# ============================================================
# 5. VALIDATED PRODUCT
# ============================================================

@app.post("/products/validated")
def create_validated_product(product: ProductValidated):
    return {
        "message": "Product is valid",
        "product": product
    }


# ============================================================
# 6. GET PRODUCT EXAMPLE
# ============================================================

@app.get("/products/{product_id}")
def get_product(product_id: int):
    return {
        "product_id": product_id
    }