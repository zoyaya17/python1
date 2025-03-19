from flask import Flask, request

app = Flask(__name__)

@app.route("/", methods=['GET'])
def great():

    print(request)
    name = request.args.get('name', '')
    print(name)

    return '<h1> Hello, ' + str(name) + '!<br> You are running Python FLASK</h1>'

@app.route("/sum/", methods=['GET'])
def sum():
    print(request)
    a = float(request.args.get('a', ''))
    b = float(request.args.get('b', ''))
    print(a, b)

    sum = a + b

    return '<h1>SUM a & b = ' + str(sum) + '</h1>'

@app.route("/sub/", methods=['GET'])
def sub():
    print(request)
    a = float(request.args.get('a', ''))
    b = float(request.args.get('b', ''))
    print(a, b)

    sub = a - b

    return '<h1>SUBTRACTION a & b = ' + str(sub) + '</h1>'

@app.route("/mul/", methods=['GET'])
def mul():
    print(request)
    a = float(request.args.get('a', ''))
    b = float(request.args.get('b', ''))
    print(a, b)

    mul = a * b

    return '<h1>MULTIPLICATION a & b = ' + str(mul) + '</h1>'

@app.route("/div/", methods=['GET'])
def div():
    print(request)
    a = float(request.args.get('a', ''))
    b = float(request.args.get('b', ''))
    print(a, b)

    div = a / b

    return '<h1>DIVISION a & b = ' + str(div) + '</h1>'