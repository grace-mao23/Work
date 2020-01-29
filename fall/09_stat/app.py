from flask import Flask
app = Flask(__name__) #create instance of class Flask

@app.route("/") #assign following function to run when root route requested
def hello_world():
    print(__name__) #prints to terminal
    return "Hello World!"
d = [0, 1, 1, 2, 3, 5, 8]
@app.route("/my_template")


if __name__ == "__main__":
    app.debug = True #defaults to False
    # allows you to make changes without restarting the terminal action
    app.run() #runs all of them
