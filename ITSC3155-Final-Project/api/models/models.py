from sqlalchemy import Boolean, Column, Integer, String, DateTime, DECIMAL, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base
from datetime import datetime
from ..dependencies.database import Base

Base = declarative_base()

class Customer(Base):
    __tablename__ = "customers"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(50))
    phone_number = Column(String(50))
    email = Column(String(50))
    address = Column(String(100))

    payments = relationship("Payment", back_populates="customers")

class MenuItem(Base):
    __tablename__ = "menu_items"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(100), unique=True, nullable=False)
    price = Column(DECIMAL(5,2), nullable=False)
    ingredients = Column(String(300), nullable=False)
    food_category = Column(String(50), nullable=False)
    calories = Column(Integer, nullable=False)

    order_details = relationship("OrderDetail", back_populates="menu_item")
    recipes = relationship("Recipe", back_populates="menu_item")

class OrderDetail(Base):
    __tablename__ = "order_details"

    id = Column(Integer, primary_key=True, index=True)
    order_id = Column(Integer, ForeignKey('orders.id'))
    item_id = Column(Integer, ForeignKey('menu_items.id'))
    quantity = Column(Integer, nullable=False)
    price = Column(DECIMAL(5, 2), nullable=False)
    
    order = relationship("Order", back_populates="order_details")
    menu_item = relationship("MenuItem")

class Order(Base):
    __tablename__ = "orders"

    id = Column(Integer, primary_key=True, index=True)
    customer_name = Column(String(100))
    order_date = Column(DateTime, nullable=False, default=datetime.now)
    tracking_num = Column(Integer, nullable=False)
    order_status = Column(String(50), nullable=False)
    price = Column(DECIMAL(5, 2), nullable=False)
    description = Column(String(300))
    takeout = Column(Boolean, nullable=False)

    order_details = relationship("OrderDetail", back_populates="order")

class Payment(Base):
    __tablename__ = "payments"

    id = Column(Integer, primary_key=True, index=True)
    customers_id = Column(Integer, ForeignKey('customers.id'))
    card_number = Column(String(20), nullable=False)
    expiration_date = Column(DateTime, nullable=False)
    transaction_status = Column(String(50), nullable=False)

    customers = relationship("Customer", back_populates="payments")

class Promotion(Base):
    __tablename__ = "promotion"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(150), unique=True)
    expiration_date = Column(String(50), nullable=False)

    promo_code = Column(String(50), unique=True) 

class Recipe(Base):
    __tablename__ = "recipes"

    id = Column(Integer, primary_key=True, index=True)
    menu_item_id = Column(Integer, ForeignKey('menu_items.id'))
    resource_id = Column(Integer, ForeignKey('resources.id'))
    amount = Column(DECIMAL(5,2), nullable=False)

    menu_item = relationship("MenuItem", back_populates="recipes")
    resource = relationship("Resource", back_populates="recipes")

class ResourceManagement(Base):
    __tablename__ = "resource_management"
    
    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    ingredient_name = Column(String(100), nullable=False)
    amount = Column(Integer, nullable=False)
    unit = Column(String(50))

class Resource(Base):
    __tablename__ = "resources"

    id = Column(Integer, primary_key=True, index=True)
    item = Column(String(100), unique=True, nullable=False)
    amount = Column(Integer, nullable=False)

    recipes = relationship("Recipe", back_populates="resource")

class Review(Base):
    __tablename__ = "Review"

    id = Column(Integer, primary_key=True, index=True)
    review = Column(String(50))
    rating = Column(Integer)