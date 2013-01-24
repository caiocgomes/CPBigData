from dbConfiguration import Base
from sqlalchemy import Column, Integer, Enum
from Util import categoricalSampler

class User(Base):
    __tablename__ = 'users'

    userid = Column(Integer, primary_key = True)
    sex = Column(Enum('M', 'F', name = 'sex'), nullable = False)
    education = Column(Integer, nullable = False)
    incomeGroup = Column(Integer, nullable = False)
    age = Column(Integer, nullable = False)
    ageGroup = Column(Integer, nullable = False)

    def __repr__(self):
        return "User({sex}, {age} years, edu:{education}, income:{incomeGroup}, ageGroup:{ageGroup})".format(
                sex = self.sex, age = self.age, education = self.education, incomeGroup = self.incomeGroup, ageGroup = self.ageGroup
                )


ageDistribution = {k : float(k**8) / float((25) + k)**16 for k in xrange(14,70)}
ageGroups = {(0,17): 0, (18,20): 1, (21,29): 2, (30,39): 3, (40,49): 4, (50,80): 5}
def educationDistribution(age):
    dage = float(age - 17)
    if age <= 17:
        return {1:1}
    elif age <= 24:
        return {1:1, 2: 0.5*dage}
    else:
        return {1 : 1, 2: 5 +0.5* dage , 3: 0.125 * dage}

def incomeDistribution(age, education):
    dage = 1 + float(age - 17)/ 20.0
    dedu = float(education - 1)
    return {1: 4, 2: 3 + 3 * dedu * dage, 3:1 + dedu * dage}

def getAgeGroup(age):
    for (age0, age1) in ageGroups.keys():
        if (age0 <= age <= age1):
            return ageGroups[(age0,age1)]
    raise ValueError("no age group = {age}".format(age=age))


def randomUser():
    sex = categoricalSampler({'M':1, 'F': 1})
    age = categoricalSampler(ageDistribution)
    education = categoricalSampler(educationDistribution(age))
    income = categoricalSampler(incomeDistribution(age, education))
    ageGroup = getAgeGroup(age)
    return User(sex = sex, age = age, education = education, incomeGroup = income, ageGroup = ageGroup)



