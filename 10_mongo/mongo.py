# Hong Wei Chen and Grace Mao: Excel
# SoftDev pd9
# K10: Import/Export Bank
# 2020-03-04

"""
Dataset:	Earth Meteorite Landings
Contains:	Information about different meteorites (space rocks) that have
			landed on Earth, including time, name, geolocation etc.
Link:		https://data.nasa.gov/resource/y77d-th95.json

Import Mechanism:	Due to the cleanness of this dataset, we only had to
					read it line by line and use the bson.json_util loads
					to insert it into our database. Loads from the package
					converts the information from JSON form into BSON form
					and makes sure it is ready to be inserted as a document.
"""
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
