from numpy import random as rnd


def categoricalSampler(pdf):
    total = float(sum(pdf.values()))
    thres = rnd.uniform()
    for k, p in pdf.items():
        thres = thres - float(p)/float(total)
        if thres < 0:
            return k
