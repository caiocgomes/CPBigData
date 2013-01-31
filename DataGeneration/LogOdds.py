from numpy import Inf, exp

class LogOddsCalculator(object):
    def __init__(self):
        self.featureSet = set()
        self.prodVector = {}
        self.featVector = {}
        self.productMatrix = {}
        self.featureMatrix = {}

    def __repr__(self):
        out = "Product Vector: " + str(self.prodVector)
        out += '\n\nFeature Vector: ' + str(self.featVector)
        out += '\n\nProduct Matrix: ' + str(self.productMatrix)
        out += '\n\nFeature Matrix: ' + str(self.featureMatrix)
        return out

    def __call__(self, product, recomendation, discount, features = {}):
        if features == {}:
            return self.logOddsPrior(product, recomendation, discount)
        else:
            logOdds = 0
            for fName, fValue in features.items():
                logOdds += self.logOdds(product, recomendation, discount, fName, fValue)
            return logOdds

    def __setitem__(self, key, value):
        if len(key) == 4:
            prod, rec, fname, fvalue = key
            self.featureMatrix[(prod.prodid, rec.prodid, fname, fvalue)] = value
            self.featureMatrix[(rec.prodid,  prod.prodid, fname, fvalue)] = value
            self.featureSet.add(fname)
        elif len(key) == 2:
            prod, rec = key
            self.productMatrix[(prod.prodid, rec.prodid)] = value
            self.productMatrix[(rec.prodid, prod.prodid)] = value
        elif len(key) == 1:
            prod = key
            self.prodVector[prod.prodid] = value
        elif len(key) == 3:
            prod, fname, fvalue = key
            self.featVector[prod.prodid, fname, fvalue] = value
            self.featureSet.add(fname)

    def __getitem__(self, key):
        if len(key) == 4:
            prod, rec, fname, fvalue = key
            return self.featureMatrix.get((prod.prodid, rec.prodid, fname, fvalue), 0)
        elif len(key) == 2:
            prod, rec = key
            return self.productMatrix.get((prod.prodid, rec.prodid), 0)
        elif len(key) == 1:
            prod, = key
            return self.prodVector.get(prod.prodid, 0)
        elif len(key) == 3:
            prod, fname, fvalue = key
            return self.featVector.get((prod.prodid, fname, fvalue), 0)

    def logOddsPrior(self, product, recomendation, discount):
        priceRatio = (float(recomendation.price) / float(product.price))
        productIndividualInfluence = self[product,] + self[recomendation,]
        productPairInfluence = self[product, recomendation]
        categoryEffect = -0.5 * float(product.category == product.category)
        return productIndividualInfluence + productPairInfluence + self.priceFunction(priceRatio) + self.discountFunction(discount) + categoryEffect

    def logOdds(self, product, recomendation, discount, featureName, featureValue):
        featurePairEffect = self[product, recomendation, featureName, featureValue]
        featureSingleEffect = self[product, featureName, featureValue] + self[recomendation, featureName, featureValue]
        discountEffect = self.discountFunction(discount, featName = featureName, featValue = featureValue)
        return self.logOddsPrior(product, recomendation, discount) + featureSingleEffect + featurePairEffect + discountEffect

    def priceFunction(self, ratio):
        out = (1.0 - ratio) ** 21 / 2.0
        return out

    def discountFunction(self, d, featName = None, featValue = None):
        out = (d/0.15)
        if featName == 'usrIncome':
            return out * (2.0 - featValue)
