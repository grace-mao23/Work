import pymongo, json, pprint
from bson.json_util import loads

client = pymongo.MongoClient('localhost', 27017) # port 27017
db = client['Excel'] # team name as database name
col = db['meteorites'] # creating collection for NASA data

if (col.count() == 0): # if it's not already in the database
	file = open("dataset.json", "r")
	data = file.readlines()
	for line in range(len(data)):
		if line == 0:
			col.insert_one(loads(data[line]))
		else:
			col.insert_one(loads(data[line][1:]))

# given a letter, return meteorites with names starting with that letter
def name(a):
    for r in col.find({}):
        if r['name'][0] == a:
            pprint.pprint(r)

### TEST CASES ###
name("A")


client.close() # at the very end !!!
