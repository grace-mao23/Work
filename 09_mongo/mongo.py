import pymongo, json

client = pymongo.MongoClient('localhost', 27017) # port 27017
db = client['testdata'] # does not have to exist
collection = db['restaurants']

def borough(b):
    query = { "borough": b }
    results = collection.find(query)
    for x in results:
        print(x)

borough("Manhattan")

client.close() # at the very end !!!
