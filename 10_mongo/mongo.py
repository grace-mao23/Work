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

# given a mass, return meteorites with mass within 50 kg of that mass
def mass(n):
	for r in col.find({ 'mass': {"$exists": True} }):
		if abs(n - float(r['mass'])) <= 50:
			pprint.pprint(r)

# given a mass, return meteorites with mass larger than that mass
def biggest(n):
	for r in col.find({ 'mass': {"$exists": True} }):
		if float(r['mass']) > n:
			pprint.pprint(r)

# given a year, return meteorites that landed in that year
def year(n):
	for r in col.find({ 'year': {"$exists": True} }):
		if float(r['year'][:4]) == n:
			pprint.pprint(r)

# the equator is at latitude 0 degrees
# each degree of latitude is 68.703 miles

# given a number of miles, return meteorites that landed within that
# number of miles from the equator in terms of latitude (given by reclat)

def lat(n):
	degrees = n / 68.703
	for r in col.find({ 'reclat': {"$exists": True} }):
		if abs(float(r['reclat'])) <= degrees:
			pprint.pprint(r)

### TEST CASES ###
#name("A")
#mass(2020)
#biggest(10000)
#year(1922)
lat(100)

client.close() # at the very end !!!
