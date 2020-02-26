import pymongo, json

client = pymongo.MongoClient('localhost', 27017) # port 27017
db = client['testdata'] # does not have to exist
collection = db['restaurants']


client.close() # at the very end !!!
