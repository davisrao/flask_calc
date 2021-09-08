# Put your app in here.
from flask import Flask, request
from operations import add, sub, mult, div

# is there a more efficient way to import?


app = Flask(__name__)

#4 different routes, add, sub, mult, div
# each route does operation from URL get style query param

@app.get('/add')
def return_sum():
    a = int(request.args["a"])
    b = int(request.args["b"])
    return f"{add(a,b)}"

@app.get('/sub')
def return_sub():
    a = int(request.args["a"])
    b = int(request.args["b"])
    return f"{sub(a,b)}"

@app.get('/mult')
def return_mult():
    a = int(request.args["a"])
    b = int(request.args["b"])
    return f"{mult(a,b)}"

@app.get('/div')
def return_div():
    a = int(request.args["a"])
    b = int(request.args["b"])
    return f"{div(a,b)}"

@app.get('/math/<operation_type>')
def return_math(operation_type):
    if operation_type == "add":
        return return_sum()

    elif operation_type == "sub":
        return return_sub()
    elif operation_type == "mult":
        return return_mult()
    elif operation_type == "div":
        return return_div()
    else: 
        return "Invalid operation"


# didnt work without return return_sum()
# can we do a = int(request.args["a"]) outside of fxns?
# is there a more efficient way to import fxns at top?