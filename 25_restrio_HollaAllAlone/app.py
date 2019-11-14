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


if __name__ == "__main__":
    app.debug = True
    app.run()
