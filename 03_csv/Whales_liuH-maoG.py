import random
import csv

workersAndPercent = {}
with open('occupations.csv') as csvfile:
    readCSV = csv.reader(csvfile, delimiter=',')
    for row in readCSV:
        if row[0] != 'Job Class':
            workersAndPercent[row[0]] = float(row[1])
    workersAndPercent.pop('Total',99.8)

def randomO(d):
    bigL = list()
    for key,value in d.items():
        bigL += [key] * int(value * 10)
    return random.choice(bigL)

print(randomO(workersAndPercent))
