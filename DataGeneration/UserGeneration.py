from Util import categoricalSampler

sexDistribution = {'M': 1, 'F': 1}
ageGroupDistribution = {0: 1, 1: 3, 2: 2, 3: 1}

def educationDistribution(ageGroup):
    if ageGroup == 0:
        return {0: 3, 1: 1}
    elif ageGroup == 1:
        return {0: 1, 1: 3}
    elif ageGroup == 2:
        return {0: 1, 1: 5, 2: 1}
    elif ageGroup == 3:
        return {0: 1, 1: 7, 2: 3}

def incomeDistribution(age, edu):
    return {0: 1,
            1: 1 + 5 * edu * age,
            2: 0.1 + edu * edu * age/2.0}

sexSampler = categoricalSampler(sexDistribution)
ageGroupSampler = categoricalSampler(ageGroupDistribution)

def educationSampler(age):
    return categoricalSampler(educationDistribution(age))()

def incomeSampler(age, edu):
    return categoricalSampler(incomeDistribution(age, edu))()
