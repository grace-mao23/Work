#Grace Mao
#SoftDev1 pd9
#K08 -- Lemme Flask You Sump'n/Three App Routes
#2019-09-18

from flask import Flask
app = Flask(__name__) #create instance of class Flask

@app.route("/") #assign following function to run when root route requested
def hello_world():
    #print("YES")
    print(__name__) #prints to terminal
    #print("NO")
    return "Hello World!"

@app.route("/espanol") #changing the address
def hola_world():
    print(__name__)
    return "Hola Mundo!"

@app.route("/frances")
def bonjour_world():
    print(__name__)
    return "Bonjour Monde!"

if __name__ == "__main__":
    app.debug = True #defaults to False
    # allows you to make changes without restarting the terminal action
    app.run() #runs all of them
