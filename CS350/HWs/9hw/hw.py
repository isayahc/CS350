
people = [{'name': "Amy", 'pounds_weight': 152, 'inches_height': 63},
{'name': "Joe", 'pounds_weight': 120, 'inches_height': 64},
 {'name': "Tom", 'pounds_weight': 210, 'inches_height': 78},
 {'name': "Jim", 'pounds_weight': 180, 'inches_height': 68},
 {'name': "Jen", 'pounds_weight': 120, 'inches_height': 62},
 {'name': "Ann", 'pounds_weight': 252, 'inches_height': 63},
 {'name': "Ben", 'pounds_weight': 240, 'inches_height': 72}]

poundsToKg = lambda x : x*0.4535924
inchesToMeters = lambda x: x*0.0254
isOverWeight = lambda x : x["BMI"] >25 and x["BMI"] <30
isObese = lambda x : x["BMI"] > 30

def addBMI(person):
    person["BMI"] = poundsToKg(person['pounds_weight'])/inchesToMeters(person['inches_height'])**2
    return person

Obese_people = list(filter(isObese, list(map(addBMI,people))))
OverWeight_people = list(filter(isOverWeight , list(map(addBMI,people))))


listform = lambda x : (("{}\n ")*len(x)).format(*x)
print(listform(Obese_people))