from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return "Hello World!"

@app.route('/blafasel')
@app.route('/index')
def index():
    a = 2
    b = 3
    c = a+b
    d = str(c)
    return d
