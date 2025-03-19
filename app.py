from flask import Flask, request, render_template
import random
import os

app = Flask(__name__)

def getRandColor():
    r = str(int(random.random() * 255))
    g = str(int(random.random() * 255))
    b = str(int(random.random() * 255))
    return f'rgb({r},{g},{b})'

@app.route("/", methods=['GET'])
def great():
    name = request.args.get('name', 'User')
    color = getRandColor()
    return render_template("navigation.html", content=f'<h1 style="font-size: 100px; text-align: center; color: {color}">Hello, {name}!<br> You are running Python FLASK</h1>')

@app.route("/calculate/", methods=['GET', 'POST'])
def calculate():
    result = None
    error = None
    a = request.args.get('a', '')
    b = request.args.get('b', '')
    operation = request.args.get('operation', 'sum')

    if a and b:
        try:
            a = float(a)
            b = float(b)
            if operation == "sum":
                result = a + b
                operation_text = "SUM"
            elif operation == "sub":
                result = a - b
                operation_text = "SUBTRACTION"
            elif operation == "mul":
                result = a * b
                operation_text = "MULTIPLICATION"
            elif operation == "div":
                if b == 0:
                    error = "Error: Division by zero!"
                else:
                    result = a / b
                    operation_text = "DIVISION"
        except ValueError:
            error = "Invalid input. Please enter numbers."

    color = getRandColor()
    
    if error:
        content = f'<h1 style="font-size: 100px; text-align: center; color: red">{error}</h1>'
    elif result is not None:
        content = f'<h1 style="font-size: 100px; text-align: center; color: {color}">{operation_text} a & b = {result}</h1>'
    else:
        content = ''

    return render_template("navigation.html", content=content, form=True)

@app.route("/col/", methods=['GET'])
def col():
    color = getRandColor()
    return render_template("navigation.html", content=f'<h1 style="font-size: 100px; text-align: center; color: {color}">RANDOM COLOR: {color}</h1>')

@app.route("/doc/", methods=['GET'])
def doc():
    try:
        # Відкриваємо та читаємо README.md як HTML
        with open("templates/readme.html", "r", encoding="utf-8") as file:
            content = file.read()
    except FileNotFoundError:
        content = "<h1>README.md not found</h1>"

    return render_template("navigation.html", content=content)

