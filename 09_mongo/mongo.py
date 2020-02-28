# Grace Mao, Alice Ni
# SoftDev pd9
# K09 -- Yummy Mongo Py
# 2020-02-28

import pymongo, json, pprint
from bson.json_util import loads

client = pymongo.MongoClient('localhost', 27017) # port 27017
db = client['testdata'] # does not have to exist
col = db['restaurants']

if (col.count() == 0): # if it's not already in the database
    file = open("dataset.json", "r")
    content = file.readlines()
    for line in content:
        col.insert_one(loads(line))

# given a borough, list out all the restaurants in that borough
def borough(b):
    for r in col.find({ "borough": b }):
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

# given a pair of coordinates, list out all the restaurants
# within 0.01 degrees of that position

# uses MANHATTAN DISTANCE
# each degree is roughly 69 miles
# because the restaurants are usually grouped together,
# the distance requirement is 0.01
def cor(x, y):
    for r in col.find({}):
        restx = r['address']['coord'][0]
        resty = r['address']['coord'][1]
        distance = abs(restx - x) + abs(resty - y)
        #print(distance)
        if (distance <= 0.01):
            pprint.pprint(r)

### TEST CASES ###
borough("Manhattan")
zipcode("10014")
grade("10014", 'A')
thres("10014", 'A')
cor(-74.0, 40.7) # usually coordinates in this dataset are around (-74.0, 40.7)

client.close() # at the very end !!!
