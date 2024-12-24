#Write 3 endpoints in Fastapi
# 1. userlogin with authentiocation
# 2. get dashboard
# 3. add item
from fastapi import FastAPI, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from pydantic import BaseModel
from typing import List

app = FastAPI()

# Mock database
fake_users_db = {
    "user1": {
        "username": "user1",
        "full_name": "User One",
        "email": "user1@example.com",
        "hashed_password": "fakehashedpassword",
        "disabled": False,
    }
}

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

class User(BaseModel):
    username: str
    email: str
    full_name: str | None = None
    disabled: bool | None = None

class UserInDB(User):
    hashed_password: str

class Item(BaseModel):
    name: str
    description: str | None = None
    price: float
    tax: float | None = None

def fake_hash_password(password: str):
    return "fakehashed" + password

def get_user(db, username: str):
    if username in db:
        user_dict = db[username]
        return UserInDB(**user_dict)

def fake_decode_token(token):
    user = get_user(fake_users_db, token)
    return user

async def get_current_user(token: str = Depends(oauth2_scheme)):
    user = fake_decode_token(token)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid authentication credentials",
            headers={"WWW-Authenticate": "Bearer"},
        )
    return user

async def get_current_active_user(current_user: User = Depends(get_current_user)):
    if current_user.disabled:
        raise HTTPException(status_code=400, detail="Inactive user")
    return current_user

@app.post("/token")
async def login(form_data: OAuth2PasswordRequestForm = Depends()):
    user_dict = fake_users_db.get(form_data.username)
    if not user_dict:
        raise HTTPException(status_code=400, detail="Incorrect username or password")
    user = UserInDB(**user_dict)
    hashed_password = fake_hash_password(form_data.password)
    if not hashed_password == user.hashed_password:
        raise HTTPException(status_code=400, detail="Incorrect username or password")
    return {"access_token": user.username, "token_type": "bearer"}

@app.get("/dashboard")
async def read_dashboard(current_user: User = Depends(get_current_active_user)):
    return {"msg": "Welcome to your dashboard", "user": current_user}

@app.post("/items/")
async def create_item(item: Item, current_user: User = Depends(get_current_active_user)):
    return {"msg": "Item added", "item": item, "user": current_user}

#Design database for an e-commerce platform
from sqlmodel import SQLModel, Field, Relationship
from typing import List, Optional
from datetime import datetime

class User(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    username: str
    email: str
    full_name: Optional[str] = None
    hashed_password: str
    disabled: Optional[bool] = None

    orders: List["Order"] = Relationship(back_populates="user")

class Product(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    name: str
    description: Optional[str] = None
    price: float
    stock: int

    order_items: List["OrderItem"] = Relationship(back_populates="product")

class Order(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    user_id: int = Field(foreign_key="user.id")
    created_at: datetime = Field(default_factory=datetime.utcnow)
    status: str

    user: User = Relationship(back_populates="orders")
    order_items: List["OrderItem"] = Relationship(back_populates="order")

class OrderItem(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    order_id: int = Field(foreign_key="order.id")
    product_id: int = Field(foreign_key="product.id")
    quantity: int

    order: Order = Relationship(back_populates="order_items")
    product: Product = Relationship(back_populates="order_items")

class Cart(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    user_id: int = Field(foreign_key="user.id")

    user: User = Relationship()
    cart_items: List["CartItem"] = Relationship(back_populates="cart")

class CartItem(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    cart_id: int = Field(foreign_key="cart.id")
    product_id: int = Field(foreign_key="product.id")
    quantity: int

    cart: Cart = Relationship(back_populates="cart_items")
    product: Product = Relationship()

# Create the database and tables
from sqlmodel import create_engine, SQLModel

DATABASE_URL = "sqlite:///./ecommerce.db"
engine = create_engine(DATABASE_URL)

def create_db_and_tables():
    SQLModel.metadata.create_all(engine)

if __name__ == "__main__":
    create_db_and_tables()


#Actual dIfferences between Django & FastAPI
# Here are the actual differences between Django and FastAPI:

# Django
# Framework Type: Full-stack web framework.
# Speed: Slower compared to FastAPI due to synchronous nature.
# ORM: Built-in ORM (Django ORM).
# Templating: Built-in templating engine.
# Admin Interface: Built-in admin interface for managing models.
# Authentication: Built-in authentication system.
# Routing: URL routing with regular expressions.
# Middleware: Extensive middleware support.
# Asynchronous Support: Limited, primarily synchronous.
# Community & Ecosystem: Large community, extensive third-party packages.
# FastAPI
# Framework Type: Modern, fast (high-performance), web framework for building APIs with Python 3.6+.
# Speed: Faster due to asynchronous support.
# ORM: No built-in ORM, but can use SQLAlchemy, Tortoise-ORM, etc.
# Templating: No built-in templating engine, but can use Jinja2, etc.
# Admin Interface: No built-in admin interface.
# Authentication: No built-in authentication system, but can use OAuth2, JWT, etc.
# Routing: Path and query parameter routing with type hints.
# Middleware: Supports Starlette middleware.
# Asynchronous Support: Fully asynchronous, built on top of Starlette and Pydantic.
# Community & Ecosystem: Growing community, fewer third-party packages compared to Django.
# Summary
# Django is a full-stack framework suitable for building complex web applications with built-in features like 
# ORM, templating, and admin interface.FastAPI is a modern, high-performance framework ideal for building APIs
#  with asynchronous support and type hints, but requires additional packages for ORM, templating, and 
# authentication. Choose Django for full-stack applications with built-in features, and FastAPI for 
# high-performance, asynchronous APIs.