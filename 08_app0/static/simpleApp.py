from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello_world():
    #print("YES")
    print(__name__)
    return "Hello World!"

@app.route("/espanol")
def hola_world():
    print(__name__)
    return "Hola Mundo!"

@app.route("/frances")
def bonjour_world():
    print(__name__)
    return "Bonjour Monde!"

if __name__ == "__main__":
    app.debug = True
    app.run()
