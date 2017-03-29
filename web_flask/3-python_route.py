#!/usr/bin/python3
from flask import Flask
app = Flask(__name__)


@app.route('/')
def hello_HBNB():
    return 'Hello HBNB!'


@app.route('/hbnb')
def HBNB():
    return 'HBNB'


@app.route('/c/<text>')
def c(text):
    return 'C {}'.format(text)


@app.route('/python/')
@app.route('/python/<text>')
def myPython(text="is cool"):
    return 'Python {}'.format(text.replace('_', ' '))

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
