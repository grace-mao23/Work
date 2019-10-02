#Team Flag - Brandon Chen, Tammy Chen. Grace Mao
#SoftDev1 pd9
#K15 -- Do I Know You?
#2019-10-02

from flask import Flask, render_template, request, redirect, url_for, session
import os
app = Flask(__name__)

#hardcoded username and passwords
user = "flag"
pword = "jamaica"
app.secret_key = os.urandom(32)

@app.route("/")
def home():
    if "loggedIn" in session:
        return redirect("/welcome")
    else:
        return redirect("/login")

@app.route("/welcome")
def welcome():
    #print(request.args)
    return render_template('template.html')

@app.route("/logout")
def logout():
    #print(request.args)
    return render_template('logout.html')

@app.route("/login")
def login():
    return render_template('login.html')

if __name__ == "__main__":
    app.debug = True
    app.run()
