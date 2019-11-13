#Grace Mao
#SoftDev1 pd9
#K24 -- A RESTful Journey Skyward
#2019-11-13

from flask import Flask, render_template
import urllib.request as urllib
import json

app = Flask(__name__) #create instance of class Flask

@app.route("/") #assign following function to run when root route requested
def home():
    urlString = "https://api.nasa.gov/mars-photos/api/v1/rovers/curiosity/photos?sol=1000&camera=rhaz&api_key=Sm9dtpNyUcONigbpXjXHFztgl0mlsjSaAhs2K8uK"
    url = urllib.urlopen(urlString)
    dict = json.loads(url.read())
    print(type(dict))
    return render_template("template.html", title="Mars Rover",
                                            collection=dict["photos"],
                                            description=lambda x: description(x))

def description(dict):
    return """ Photo taken by the Mars Rover {0} by the {1} on {2}.
            The {0} landed on Mars on {3}, launching from earth on {4}.
            It is currently {5}.""".format(
                dict["rover"]["name"], dict["camera"]["full_name"],
                dict["earth_date"], dict["rover"]["landing_date"],
                dict["rover"]["launch_date"], dict["rover"]["status"]
            )

if __name__ == "__main__":
    app.debug = True #defaults to False
    # allows you to make changes without restarting the terminal action
    app.run() #runs all of them
