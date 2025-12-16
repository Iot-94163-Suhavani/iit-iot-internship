def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a,b):
    return a * b

def division(a,b):
    return a / b

def calculate(operation, x, y):
    return operation(x, y)

# Passing functions
print(calculate(add, 10, 5))
print(calculate(subtract, 10, 5))
print(calculate(multiply, 10, 5))
print(calculate(division, 10, 5))
