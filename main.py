from flask import Flask

app = Flask(__name__)

@app.route("/Home")
def hello_world():
    return '<h1>Hello, This is the second page!</h1>'

@app.route("/Page2")
def Pagetwo():
    return '<h1>Hello, this is the second page!</h1>'

app.run(debug=True)