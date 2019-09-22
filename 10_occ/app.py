#Grace Mao
#SoftDev1 pd9
#K10 -- Jinja Tuning
#2019-09-24

from flask import Flask, render_template
app = Flask(__name__)

@app.route("/") #root
def home():
    print(__name__)
    return "Go to /occupyflaskst"

@app.route('/occupyflaskst')
def occupy():
    
