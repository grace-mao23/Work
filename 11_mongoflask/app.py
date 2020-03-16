from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def hello_world():
    #print("YES")
    print(__name__)
    return render_template("base.html")

if __name__ == "__main__":
    app.debug = True
    app.run()
