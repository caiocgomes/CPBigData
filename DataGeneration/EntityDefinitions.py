# -*- coding: utf-8 -*-
from collections import namedtuple
from UserGeneration import sexSampler, educationSampler, incomeSampler, ageGroupSampler

class Product(namedtuple('Product', "prodid name category price") ):
    _lastid = 0

    def __new__(cls, name, category, price):
        cls._lastid += 1
        return super(Product, cls).__new__(cls, cls._lastid, name, category, price)

class User(namedtuple('User', "userid sex education incomeGroup ageGroup")):

    _lastid = 0

    def __new__(cls):
        cls._lastid += 1
        sex = sexSampler()
        ageGroup = ageGroupSampler()
        education = educationSampler(ageGroup)
        incomeGroup = incomeSampler(ageGroup, education)
        return super(User, cls).__new__(cls, cls._lastid, sex, education, incomeGroup, ageGroup)
