import pymongo, json, pprint

client = pymongo.MongoClient('localhost', 27017) # port 27017
db = client['testdata'] # does not have to exist
col = db['restaurants']

def borough(b):
    for r in col.find({ "borough": b }):
        pprint.pprint(r)

def zipcode(z):
    for r in col.find({ "zipcode": z }):
        pprint.pprint(r)


### TEST CASES
# borough("Manhattan")
zipcode("10282")

client.close() # at the very end !!!
