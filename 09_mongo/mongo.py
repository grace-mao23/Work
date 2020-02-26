import pymongo, json

client = pymongo.MongoClient('localhost', 27017) # port 27017
db = client['testdata'] # does not have to exist
col = db['restaurants']

def borough(b):
    for r in col.find({ "borough": b }):
        pprint.pprint(r)

borough("Manhattan")

client.close() # at the very end !!!
