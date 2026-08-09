from fastapi import FastAPI, HTTPException, Depends
from pydantic import BaseModel
from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.orm import sessionmaker, declarative_base, Session

app = FastAPI()


# ============================================================
# DATABASE CONFIGURATION
# ============================================================

DATABASE_URL = "sqlite:///./products.db"


engine = create_engine(
    DATABASE_URL,
    connect_args={
        "check_same_thread": False
    }
)


SessionLocal = sessionmaker(
    autocommit=False,
    autoflush=False,
    bind=engine
)


Base = declarative_base()


# ============================================================
# SQLALCHEMY DATABASE MODEL
# ============================================================

class ProductDB(Base):

    __tablename__ = "products"

    id = Column(
        Integer,
        primary_key=True,
        index=True
    )

    title = Column(
        String,
        nullable=False
    )

    category = Column(
        String,
        nullable=False
    )

    price = Column(
        Integer,
        nullable=False
    )

    size = Column(
        String,
        nullable=False
    )


# ============================================================
# CREATE DATABASE TABLES
# ============================================================

Base.metadata.create_all(
    bind=engine
)


# ============================================================
# PYDANTIC MODEL
# ============================================================

class Product(BaseModel):

    title: str
    category: str
    price: int
    size: str


# ============================================================
# DATABASE SESSION
# ============================================================

def get_db():

    db = SessionLocal()

    try:
        yield db

    finally:
        db.close()


# ============================================================
# HOME
# ============================================================

@app.get("/")
def home():

    return {
        "message": "Lesson 7 - SQLAlchemy"
    }


# ============================================================
# CREATE PRODUCT
# POST /products
# ============================================================

@app.post("/products")
def create_product(
    product: Product,
    db: Session = Depends(get_db)
):

    new_product = ProductDB(
        title=product.title,
        category=product.category,
        price=product.price,
        size=product.size
    )

    db.add(new_product)

    db.commit()

    db.refresh(new_product)

    return {
        "message": "Product created successfully",
        "product": {
            "id": new_product.id,
            "title": new_product.title,
            "category": new_product.category,
            "price": new_product.price,
            "size": new_product.size
        }
    }


# ============================================================
# READ ALL PRODUCTS
# GET /products
# ============================================================

@app.get("/products")
def get_products(
    db: Session = Depends(get_db)
):

    products = db.query(ProductDB).all()

    return {
        "count": len(products),
        "products": [
            {
                "id": product.id,
                "title": product.title,
                "category": product.category,
                "price": product.price,
                "size": product.size
            }
            for product in products
        ]
    }


# ============================================================
# READ ONE PRODUCT
# GET /products/{product_id}
# ============================================================

@app.get("/products/{product_id}")
def get_product(
    product_id: int,
    db: Session = Depends(get_db)
):

    product = db.query(ProductDB).filter(
        ProductDB.id == product_id
    ).first()

    if product is None:

        raise HTTPException(
            status_code=404,
            detail="Product not found"
        )

    return {
        "id": product.id,
        "title": product.title,
        "category": product.category,
        "price": product.price,
        "size": product.size
    }


# ============================================================
# UPDATE PRODUCT
# PUT /products/{product_id}
# ============================================================

@app.put("/products/{product_id}")
def update_product(
    product_id: int,
    product: Product,
    db: Session = Depends(get_db)
):

    existing_product = db.query(ProductDB).filter(
        ProductDB.id == product_id
    ).first()

    if existing_product is None:

        raise HTTPException(
            status_code=404,
            detail="Product not found"
        )

    existing_product.title = product.title
    existing_product.category = product.category
    existing_product.price = product.price
    existing_product.size = product.size

    db.commit()

    db.refresh(existing_product)

    return {
        "message": "Product updated successfully",
        "product": {
            "id": existing_product.id,
            "title": existing_product.title,
            "category": existing_product.category,
            "price": existing_product.price,
            "size": existing_product.size
        }
    }


# ============================================================
# DELETE PRODUCT
# DELETE /products/{product_id}
# ============================================================

@app.delete("/products/{product_id}")
def delete_product(
    product_id: int,
    db: Session = Depends(get_db)
):

    product = db.query(ProductDB).filter(
        ProductDB.id == product_id
    ).first()

    if product is None:

        raise HTTPException(
            status_code=404,
            detail="Product not found"
        )

    db.delete(product)

    db.commit()

    return {
        "message": "Product deleted successfully",
        "product_id": product_id
    }