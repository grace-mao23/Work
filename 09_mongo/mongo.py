import pymongo, json, pprint
from bson.json_util import loads

client = pymongo.MongoClient('localhost', 27017) # port 27017
db = client['testdata'] # does not have to exist
col = db['restaurants']

if (restaurants.count() == 0):
    file = open("dataset.json", "r")
    content = file.readlines()
    for line in content:
        restaurants.insert_one(loads(line))

def borough(b):
    for r in col.find({ "borough": b }):
        pprint.pprint(r)

def zipcode(z):
    for r in col.find({ "zipcode": z }):
        pprint.pprint(r)


### TEST CASES
# borough("Manhattan")
#zipcode("10282")

client.close() # at the very end !!!
