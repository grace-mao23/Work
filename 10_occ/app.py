#Grace Mao
#SoftDev1 pd9
#K10 -- Jinja Tuning
#2019-09-24

from flask import Flask, render_template
# CODE FROM 03_CSV
import random
import csv

workersAndPercent = {}
with open('occupations.csv') as csvfile:
    readCSV = csv.reader(csvfile, delimiter=',')
    for row in readCSV: #for each row in the csv file
        if row[0] != 'Job Class': #as long as it's not the first row
            workersAndPercent[row[0]] = float(row[1]) #turn value into a float
    workersAndPercent.pop('Total',99.8) #pop off the last row

def randomO(d):
    bigL = list()
    for key,value in d.items():
        bigL += [key] * int(value * 10) #add each job to the list value*10 many times
    return random.choice(bigL) #weighted random choice based on how many times a job is in the list

app = Flask(__name__)

@app.route("/") #root
def home():
    print(__name__)
    return "Go to /occupyflaskst"

@app.route('/occupyflaskst')
def occupy():

if __name__ == "__main__":
    app.debug = True
    app.run()
