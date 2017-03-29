#!/usr/bin/python3
from flask import Flask, render_template
app = Flask(__name__)


@app.route('/')
def hello_HBNB():
    return 'Hello HBNB!'


@app.route('/hbnb')
def HBNB():
    return 'HBNB'


@app.route('/c/<text>')
def c(text):
    return 'C {}'.format(text.replace('_', ' '))


@app.route('/python/')
@app.route('/python/<text>')
def myPython(text="is cool"):
    return 'Python {}'.format(text.replace('_', ' '))


@app.route('/number/<int:n>')
def number(n):
    return '{} is a number'.format(n)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
