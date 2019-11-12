#Grace Mao
#SoftDev1 pd9
#K24 -- A RESTful Journey Skyward
#2019-11-13

from flask import Flask, render_template
import urllib3, json

app = Flask(__name__) #create instance of class Flask

@app.route("/") #assign following function to run when root route requested
def home():
    url = "https://api.nasa.gov/mars-photos/api/v1/rovers/curiosity/photos?sol=1000&camera=rhaz&api_key=Sm9dtpNyUcONigbpXjXHFztgl0mlsjSaAhs2K8uK"
    dict = urllib3.urlopen(url)
    head = urllib3.info(url)
    return render_template("template.html", title=head)

if __name__ == "__main__":
    app.debug = True #defaults to False
    # allows you to make changes without restarting the terminal action
    app.run() #runs all of them
