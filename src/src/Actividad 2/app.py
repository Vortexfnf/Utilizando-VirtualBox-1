from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello_world():
    return '<h1>Hello, World!</h1>'

@app.route("/Page2")
def Page2():
    return '<h1>Hello, welcome to the second page!</h1>'

app.run(debug=True)