import random as rand

def randomStudent(d):
    teams = list() # create new list
    for key in d.keys(): # d.keys() list NOT indexable
        teams.append(key)
    team = teams[rand.randint(0,len(teams)-1)] # select the random team
    student = d[team][rand.randint(0,len(d)-1)] # select the random student from team
    print (student) # print it
    # return nothing

KREWES = { 'orpheus':['Emily','Kevin'], 'rex':['Joey','Jackie'] }

randomStudent(KREWES);
