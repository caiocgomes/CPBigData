from Values import *
from EntityDefinitions import User
from random import choice, uniform
from math import exp
from numpy import mean
from time import sleep
import operator

users = [User() for i in xrange(500)]
discounts = [0.05, 0.10, 0.15]

def features(user):
    return {'usrAge': user.ageGroup,
            'usrEdu': user.education,
            'usrSex': user.sex,
            'usrIncome': user.incomeGroup}

def getRecomendation(prod):
    rec = choice(prods)
    while prod.prodid == rec.prodid:
        rec = choice(prods)
    return rec

def compra(p):
    quer = (uniform(0,1) < p)
    return (uniform(0,1) < (0.2 if quer else 0.0001))

def evalCompras():
    prod = robot 
    res = {}
    for rec in prods:
        prob = {True: [], False:[]}
        conversion = 0.0
        for _ in xrange(10000):
            user = User()
            discount = choice(discounts)

            loddsPrior = LOdds(prod, rec, discount)
            loddsFeatures = LOdds(prod, rec, discount, features = features(user))
            exponent = 3.0 * loddsPrior - loddsFeatures
            p = 1.0/(1.0 + exp(exponent if exponent < 100.0 else 100.0))

            compraJunto = compra(p)
            conversion += compraJunto
            prob[compraJunto].append(p)
            res[rec] = conversion/10000.0

    print prod.name
    print "======"
    for k,v in sorted(res.items(), key=operator.itemgetter(1), reverse = True):
        print k.name, v

def calcProbability(prod, rec, user, discount):
    loddsPrior = LOdds(prod, rec, discount)
    loddsFeatures = LOdds(prod, rec, discount, features = features(user))
    exponent = 3.0 * loddsPrior - loddsFeatures
    p = 1.0/(1.0 + exp(exponent if exponent < 100.0 else 100.0))
    return p

def genCompra():
    prod = choice(prods)
    rec = getRecomendation(prod)
    user = User()
    discount = choice(discounts)
    p = calcProbability(prod, rec, user, discount)
    return prod.prodid, rec.prodid, discount, user.sex, user.ageGroup, user.education, user.incomeGroup, int(compra(p))

def generateNewBuys(n = 0):
    if n <= 0:
        while True:
            yield genCompra()
    else:
        for i in xrange(n):
            yield genCompra()

