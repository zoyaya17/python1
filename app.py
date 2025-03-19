from flask import Flask, request
from random import random

app = Flask(__name__)

def getRandColor():
    r = str(int(random.random() * 255))
    g = str(int(random.random() * 255))
    b = str(int(random.random() * 255))
    rgb = 'rgb(' + r + ',' + g + ',' + b + ')'
    return rgb 

@app.route("/", methods=['GET'])
def great():

    print(request)
    name = request.args.get('name', '')
    print(name)

    color = getRandColor()

    if name == '':
      name = 'User'

    return '<h1 style="font-size: 100px; text-align: center; color: ' + color + '">' + 'Hello, ' + str(name) + '!<br> You are running Python FLASK</h1>'

@app.route("/sum/", methods=['GET'])
def sum():
    print(request)
    a = float(request.args.get('a', ''))
    b = float(request.args.get('b', ''))
    print(a, b)

    sum = a + b

    color = getRandColor()

    return '<h1 style="font-size: 100px; text-align: center; color: ' + color + '">' + 'SUM a & b = ' + str(sum) + '</h1>'

@app.route("/sub/", methods=['GET'])
def sub():
    print(request)
    a = float(request.args.get('a', ''))
    b = float(request.args.get('b', ''))
    print(a, b)

    sub = a - b

    color = getRandColor()

    return '<h1 style="font-size: 100px; text-align: center; color: ' + color + '">' + 'SUBTRACTION a & b = ' + str(sub) + '</h1>'

@app.route("/mul/", methods=['GET'])
def mul():
    print(request)
    a = float(request.args.get('a', ''))
    b = float(request.args.get('b', ''))
    print(a, b)

    mul = a * b

    color = getRandColor()

    return '<h1 style="font-size: 100px; text-align: center; color: ' + color + '">' + 'MULTIPLICATION a & b = ' + str(mul) + '</h1>'

@app.route("/div/", methods=['GET'])
def div():
    print(request)
    a = float(request.args.get('a', ''))
    b = float(request.args.get('b', ''))
    print(a, b)

    div = a / b

    color = getRandColor()

    return '<h1 style="font-size: 100px; text-align: center; color: ' + color + '">' + 'DIVISION a & b = ' + str(div) + '</h1>'