from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, Vedant Patel & Rachana run from package!'
