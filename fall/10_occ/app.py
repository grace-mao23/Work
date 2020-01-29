#Grace Mao
#SoftDev1 pd9
#K10 -- Jinja Tuning
#2019-09-24

from flask import Flask, render_template
# CODE FROM 03_CSV
import random
import csv

workersAndPercent = {}
with open('occ2.csv') as csvfile:
    readCSV = csv.reader(csvfile, delimiter=',')
    for row in readCSV: #for each row in the csv file
        if row[0] != 'Job Class' and row[0] != 'Total': #as long as it's not the first row
            temp = list()
            temp.append(float(row[1]))
            temp.append(row[2])
            workersAndPercent[row[0]] = temp #turn value into a float
    #workersAndPercent.pop('Total',99.8) #pop off the last row

def randomO(d): # WITHOUT LINKS
    bigL = list() # will generate very large list with weighted items
    for key,value in d.items():
        bigL += [key] * int(value * 10) #add each job to the list value*10 many times
    return random.choice(bigL) #weighted random choice based on how many times a job is in the list

def rando(d): # WITH LINKS
    bigL = list()
    for key,value in d.items():
        bigL += [key] * int(value[0] * 10)
    return random.choice(bigL)

app = Flask(__name__) #instance of Flask

@app.route("/") #root
def home():
    print(__name__) #prints to terminal
    return "Go to /occupyflaskst"

@app.route('/occupyflaskst')
def occupy():
    print(__name__) #prints to terminal
    chosen = rando(workersAndPercent)
    return render_template('template.html',
                            title = 'Tablified Occupations Data',
                            heading = 'K10: Jinja Tuning',
                            h2 = 'Tablifying Occupations Data and Providing Help :)',
                            team = 'The Bears: Taejoon Kim, Grace Mao',
                            job = chosen,
                            link = workersAndPercent[chosen][1],
                            jobs = 'Occupation',
                            percent = 'Percentage',
                            collection = workersAndPercent)

if __name__ == "__main__":
    app.debug = True
    app.run()
