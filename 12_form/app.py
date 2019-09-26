from flask import Flask, render_template, request
app = Flask(__name__)

@app.route("/")
def home():
    return render_template('foo.html')

@app.route("/auth")
def maybe():
    #print (request.args)
    #print (request.method)
    #print (app)
    return render_template('poo.html',
                            name = request.args['name'],
                            args = request.method)

if __name__ == "__main__":
    app.debug = True
    app.run()
