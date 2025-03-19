from flask import Flask, request, render_template
import random
import os

app = Flask(__name__)

def getRandColor():
    r = str(int(random.random() * 255))
    g = str(int(random.random() * 255))
    b = str(int(random.random() * 255))
    rgb = f'rgb({r},{g},{b})'
    return rgb 

@app.route("/", methods=['GET'])
def great():
    name = request.args.get('name', 'User')
    color = getRandColor()
    return render_template("navigation.html", content=f'<h1 style="font-size: 100px; text-align: center; color: {color}">Hello, {name}!<br> You are running Python FLASK</h1>')

@app.route("/sum/", methods=['GET'])
def sum():
    a = float(request.args.get('a', 0))
    b = float(request.args.get('b', 0))
    result = a + b
    color = getRandColor()
    return render_template("navigation.html", content=f'<h1 style="font-size: 100px; text-align: center; color: {color}">SUM a & b = {result}</h1>')

@app.route("/sub/", methods=['GET'])
def sub():
    a = float(request.args.get('a', 0))
    b = float(request.args.get('b', 0))
    result = a - b
    color = getRandColor()
    return render_template("navigation.html", content=f'<h1 style="font-size: 100px; text-align: center; color: {color}">SUBTRACTION a & b = {result}</h1>')

@app.route("/mul/", methods=['GET'])
def mul():
    a = float(request.args.get('a', 0))
    b = float(request.args.get('b', 0))
    result = a * b
    color = getRandColor()
    return render_template("navigation.html", content=f'<h1 style="font-size: 100px; text-align: center; color: {color}">MULTIPLICATION a & b = {result}</h1>')

@app.route("/div/", methods=['GET'])
def div():
    a = float(request.args.get('a', 1))
    b = float(request.args.get('b', 1))
    if b == 0:
        return render_template("navigation.html", content='<h1 style="font-size: 100px; text-align: center; color: red">Error: Division by zero!</h1>')
    result = a / b
    color = getRandColor()
    return render_template("navigation.html", content=f'<h1 style="font-size: 100px; text-align: center; color: {color}">DIVISION a & b = {result}</h1>')

@app.route("/col/", methods=['GET'])
def col():
    color = getRandColor()
    return render_template("navigation.html", content=f'<h1 style="font-size: 100px; text-align: center; color: {color}">RANDOM COLOR: {color}</h1>')

@app.route("/doc/", methods=['GET'])
def doc():
    if os.path.exists("README.md"):
        with open("README.md", "r", encoding="utf-8") as file:
            content = file.read().replace("\n", "<br>")
    else:
        content = "<h1>README.md not found</h1>"
    return render_template("navigation.html", content=content)
