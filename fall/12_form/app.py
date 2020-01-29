#The HillBillies: Grace Mao, Jackson Zou
#SoftDev1 pd9
#K12 -- Echo echo echo
# 2019-10-02

from flask import Flask, render_template, request
app = Flask(__name__)

@app.route("/")
def home():
    return render_template('foo.html')

@app.route("/auth")
def maybe():
    # print("\n\n\n")
    # print("***DIAG: this Flask obj ***")
    # print(app)
    # print("***DIAG: request obj ***")
    # print(request)
    # print("***DIAG: request.args ***")
    # print(request.args)
    # print("***DIAG: request.args['username'] ***")
    # print(request.args['name'])
    # print("***DIAG: request.headers ***")
    # print(request.headers)
    return render_template('poo.html',
                            name = request.args['name'],
                            args = request.method)

if __name__ == "__main__":
    app.debug = True
    app.run()
