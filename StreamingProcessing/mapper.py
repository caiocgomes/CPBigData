import sys

for line in sys.stdin:
    line = line.strip().split()
    prodid, recid, discount, usrSex, usrAgeGroup, usrEducation, usrIncomeGroup, compraEfetuada = line
    print prodid, recid, discount, compraEfetuada, 'sex', usrSex
    print prodid, recid, discount, compraEfetuada, 'edu', usrEducation
    print prodid, recid, discount, compraEfetuada, 'inc', usrIncomeGroup
    print prodid, recid, discount, compraEfetuada, 'age', usrAgeGroup

