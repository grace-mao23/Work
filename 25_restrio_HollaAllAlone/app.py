#Grace Mao
#SoftDev1 pd9
#K25: Getting More REST
#2019-11-13

from flask import Flask, render_template
import urllib.request as urllib
import json

app = Flask(__name__)

@app.route("/")
def home():
   return render_template("index.html")

@app.route("/ghibli")
def ghibli():
    url = "https://ghibliapi.herokuapp.com/films/58611129-2dbc-4a81-a72f-77ddfc1b1b49"
    response = urllib.urlopen(url)
    response = response.read()
    data = json.loads(response)
    return render_template("ghibli.html", title=data['title'],
                                          desc=data['description'],
                                          director=data['director'],
                                          producer=data['producer'],
                                          rt=data['rt_score'],
                                          date=data['release_date'])

@app.route("/purgomalum")
def profanity():
    url = "https://www.purgomalum.com/service/json?text=kiss%20my%20ass%20softdev%20is%20awesome"
    response = urllib.urlopen(url)
    response = response.read()
    data = json.loads(response)
    return render_template("purgo.html", input=data['result'])

@app.route("/openlibrary")
def lib():
    url = "https://openlibrary.org/works/OL16596099W.json"
    response = urllib.urlopen(url)
    response = response.read()
    data = json.loads(response)
    url2 = "https://openlibrary.org{}.json".format(data['authors'][0]['author']['key'])
    #print(url2);
    res = urllib.urlopen(url2)
    res = res.read()
    data2 = json.loads(res)
    #print(data2)
    return render_template("library.html", title=data['title'],
                                           author=data2['name'],
                                           desc=data['description']['value'],
                                           collection=data['subjects'])


if __name__ == "__main__":
    app.debug = True
    app.run()
