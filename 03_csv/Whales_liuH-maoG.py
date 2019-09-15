import random

file = open('occupations.csv')
lines = file.readlines() # read in all lines
file.close()

lines = lines[1:len(lines)-1] # first and last line not needed
dict = dict()

for i in lines:
    newI = i.strip() # get rid of the \n
    if '\",' in newI: # if the occupation has quotes around it
        key = newI[1:newI.find('\",')]
        value = float(newI[newI.find('\",')+2:])
    else:
        key = newI[:newI.find(',')] # if it's a simple occupation
        value = float(newI[newI.find(',')+1:])
    dict[key] = value # add to dictionary

def randomO(d):
    bigL = list()
    for key,value in d.items():
        bigL += [key] * int(value * 10)
    return random.choice(bigL)

print(randomO(dict))
