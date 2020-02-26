import pymongo, json

client = pymongo.MongoClient('localhost', 27017) # port 27017
db = client['testdata'] # does not have to exist
collection = db['restaurants']

with open('dataset.json') as f:
    file_data = json.load(f.read()) # read in json file

collection.insert_many(file_data)

client.close() # at the very end !!!
