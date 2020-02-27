import pymongo, json, pprint
from bson.json_util import loads

client = pymongo.MongoClient('localhost', 27017) # port 27017
db = client['testdata'] # does not have to exist
col = db['restaurants']

if (col.count() == 0):
    file = open("dataset.json", "r")
    content = file.readlines()
    for line in content:
        col.insert_one(loads(line))

def borough(b):
    for r in col.find({ "borough": b }):
        pprint.pprint(r)

def zipcode(z):
    for r in col.find({ "address.zipcode": z }):
        pprint.pprint(r)

def grade(z, g):
    for r in col.find({ "address.zipcode": z }):
       # print(r)
        record = r['grades']
       # print(record)
    #    print(record[len(record)-1])
        if (record[len(record)-1]['grade'] == g):
            pprint.pprint(r)

def thres(z, g):
    for r in col.find({ "address.zipcode": z }):
        record = r['grades']
        for i in range(len(record)):
            if (record[i]['grade'] > (int)g):
                pprint.pprint(r)

### TEST CASES
#borough("Manhattan")
#zipcode("10014")
grade("10014", 'A')

client.close() # at the very end !!!
