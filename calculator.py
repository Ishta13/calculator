import math
def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        raise ValueError("Cannot divide by zero")
    return a / b

def square_root(a):
    if a < 0:
        raise ValueError("Cannot calculate the square root of a negative number")
    return math.sqrt(a)

def exponentiate(base, exp):
    return base ** exp

