from flask import Flask, render_template, request
app = Flask(__name__)

@app.route("/")
def home():
    return render_template('foo.html')

@app.route("/auth")
def maybe():
    print(request.form)
    print(request)
    print(request.args)
    print(request.headers)
    print(request.method)
    print(app)
    return request.args["jaco"]

if __name__ == "__main__":
    app.debug = True
    app.run()
