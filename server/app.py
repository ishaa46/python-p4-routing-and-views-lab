#!/usr/bin/env python3

from flask import Flask

app = Flask(__name__)


@app.route('/')
def index():
    return '<h1>Python Operations with Flask Routing and Views</h1>'


@app.route('/print/<string:parameter>')
def print_string(parameter):
    print(parameter)
    return parameter


@app.route('/count/<int:count>')
def count(count):
    return ''.join(f"{i}\n" for i in range(count))


@app.route('/math/<num1>/<operation>/<num2>')
def math(num1, operation, num2):
    try:
        a = int(num1)
        b = int(num2)
    except ValueError:
        return 'Invalid input', 400

    if operation == '+':
        result = a + b
    elif operation == '-':
        result = a - b
    elif operation == '*':
        result = a * b
    elif operation == 'div':
        result = a / b
    elif operation == '%':
        result = a % b
    else:
        return 'Invalid operation', 400

    return str(result)


if __name__ == '__main__':
    app.run(port=5555, debug=True)
