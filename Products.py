# -*- coding: utf-8 -*-
from dbConfiguration import Base
from sqlalchemy import Column, Integer, String

class Product(Base):
    __tablename__ = 'products'

    prodid = Column(Integer, primary_key = True)
    name = Column(String)
    category = Column(String)
    price = Column(Integer)

    def __init__(self, name, category, price):
        self.name = name
        self.category = category
        self.price = price

    def __repr__(self):
        return u"Product({name}, {cat}, R${price}.00)".format(name=self.name, cat = self.category, price=self.price)

