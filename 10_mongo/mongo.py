import pymongo, json, pprint
from bson.json_util import loads

client = pymongo.MongoClient('localhost', 27017) # port 27017
db = client['Excel'] # team name as database name
col = db['meteorites'] # creating collection for NASA data

if (col.count() == 0): # if it's not already in the database
    file = open("dataset.json", "r")
    content = file.readlines()
    for line in content:
        col.insert_one(loads(line))

# given a letter, return meteorites with names starting with that letter
def name(a):
    for r in col.find({}):
        if r['name'][0] == a:
            pprint.pprint(r)

# given a zipcode, list out all the restaurants with that zipcode
def zipcode(z):
    for r in col.find({ "address.zipcode": z }):
        pprint.pprint(r)

# given a zipcode, list out all the restaurants
# whose last grade matches the given grade
def grade(z, g):
    for r in col.find({ "address.zipcode": z }):
       # print(r)
        record = r['grades']
       # print(record)
    #    print(record[len(record)-1])
        if (record[len(record)-1]['grade'] == g):
            pprint.pprint(r)

# given a zipcode, list out all the restaurants
# with any history of a grade lower than the threshold given
def thres(z, g):
    for r in col.find({ "address.zipcode": z }):
        record = r['grades']
        for i in range(len(record)):
            if (record[i]['grade'] > g):
                pprint.pprint(r)

def cor(x, y):
    for r in col.find({}):
        restx = r['address']['coord'][0]
        resty = r['address']['coord'][1]
        distance = abs(restx - x) + abs(resty - y)
        #print(distance)
        if (distance <= 0.01):
            pprint.pprint(r)

### TEST CASES ###
name("A")


client.close() # at the very end !!!
