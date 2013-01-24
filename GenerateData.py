"""
FACTS:
    - LogOdds(X) = log[P(X is True)/ P(X is False)]
    - LogOdds(C) = -1.75
    """

logOddsOfBuyingTogether = -1.75

class LogOddsCalculator(object):
    def __init__(self):
        self.nullEffectRatio = 0.1
        self.discountEffect = 1.0
        self.productMatrix = {}
        self.featureMatrix = {}

    def __call__(self, product, recomendation, discount, features = {}):
        if features == {}:
            return self.logOddsPrior(product, recomendation, discount)
        else:
            logOdds = 0
            for fName, fValue in features.items():
                logOdds += self.logOdds(product, recomendation, discount, fName, fValue)

    def __setitem__(self, key, value):
        try:
            prod, rec, fname, fvalue = key
            self.featureMatrix[(prod.prodid, rec.prodid, fname, fvalue)] = value
        except ValueError:
            prod, rec = key
            self.productMatrix[(prod.prodid, rec.prodid)] = value

    def __getitem__(self, key):
        try:
            prod, rec, fname, fvalue = key
            return self.featureMatrix[(prod.prodid, rec.prodid, fname, fvalue)]
        except ValueError:
            prod, rec = key
            return self.productMatrix[(prod.prodid, rec.prodid)]

    def logOddsPrior(self, product, recomendation, discount):
        priceRatio = (recomendation.price / product.price)
        productInfluence = self[product, recomendation]
        return productInfluence + self.priceFunction(priceRatio) + self.discountFunction(discount)

    def logOdds(self, product, recomendation, discount, featureName, featureValue):
        featureEffect = self[product, recomendation, featureName, featureValue]
        return self.logOddsPrior(product, recomendation, discount) + featureEffect

    def priceFunction(self, ratio):
        return 1.0 - ratio / self.nullEffectRatio

    def discountFunction(self, d):
        return self.discountEffect * d
