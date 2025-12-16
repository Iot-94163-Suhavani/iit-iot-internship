#-----defaul parameters-----
def greet(name, message="Good Morning"):
    print(message, name)

greet("Alice")                
greet("Bob", "Good Evening")   

#-----key-value pair----
def student_info(name, age, course):
    print("Name:", name)
    print("Age:", age)
    print("Course:", course)

student_info(age=20, course="IoT", name="Dhanashri")
student_info(age=20, course="IoT", name="Suhavani")

#-------passing arguments------
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
