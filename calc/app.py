from flask import Flask, request


app = Flask(__name__)


@app.route('/add')
def add():
    """Add a and b."""
    a = int(request.args["a"])
    b = int(request.args["b"])
    sub = a + b
    return f"<h1>{a} + {b} is: {sub}</h1>"

@app.route('/sub')
def sub():
    """Subtract a and b."""
    a = int(request.args["a"])
    b = int(request.args["b"])
    sub =  a - b
    return f"<h1>{a} - {b} is: {sub}</h1>"
    

@app.route('/mult')
def mult():
    """Multiply a and b."""
    a = int(request.args["a"])
    b = int(request.args["b"])
    mult =  a * b
    return f"<h1>{a} * {b} is: {mult}</h1>"


@app.route('/div')
def div():
    """Divide a and b."""
    a = int(request.args["a"])
    b = int(request.args["b"])
    div = a / b
    return f"<h1>{a} / {b} is: {div}</h1>"

@app.route('/math/<calc>')
def math(calc):
    a = int(request.args["a"])
    b = int(request.args["b"])
    if calc == 'add':
        result = a + b
    elif calc == 'sub':
        result = a - b
    elif calc == 'mult':
        result = a * b
    elif calc == 'div':
        result = a / b
    else:
        return f"<h1>You did not provide a valid input</h1>"

    return f"<h1>The result is: {result}</h1>"
