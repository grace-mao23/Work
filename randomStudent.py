import random

def randomStudent(d):
    teams = list() # create new list
    for key in d.keys(): # d.keys() list NOT indexable
        teams.append(key)
    team = teams[random.randint(0,len(teams)-1)] # select the random team
    student = d[team][random.randint(0,len(team)-1)] # select the random student from team
    print (student) # print it
    # return nothing

def randomS(d):
    team = random.choice(d.values());
    print random.choice(team);

KREWES = {'orpheus':['Emily', 'Kevin', 'Vishwaa', 'Eric', 'ray', 'Jesse', 'Tiffany',
            'Amanda', 'Junhee', 'Jackie', 'Tyler', 'Emory', 'Ivan', 'Elizabeth',
            'Pratham', 'Shaw', 'Eric', 'Yaru', 'Kelvin', 'Hong Wei', 'Michael',
            'Kiran', 'Amanda', 'Joseph', 'Tanzim', 'David', 'Yevgeniy'],
        'rex':['William', 'Joseph', 'Calvin', 'Ethan', 'Moody', 'Mo', 'Big Mo',
                'Peihua', 'Saad', 'Benjamin', 'Justin', 'Alice', 'Hilary', 'Ayham',
                'Michael', 'Matthew', 'Jionghao', 'Devin', 'David', 'Jacob', 'Will',
                'Hannah', 'Alex'],
        'endymion':['Grace', 'Nahi', 'Derek', 'Jun Tao', 'Connor', 'Jason',
                'Tammy', 'Albert', 'Kazi', 'Derek', 'Brandon', 'Kenneth', 'Lauren',
                'Biraj', 'Jeff', 'Jackson', 'Taejoon', 'Kevin', 'Jude', 'Sophie', 'Henry',
                'Coby', 'Manfred', 'Leia', 'Ahmed', 'Winston']}

randomStudent(KREWES);
randomS(KREWES);
