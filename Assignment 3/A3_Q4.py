def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        return "Error! Division by zero."
    return a / b


while True:
    print("\n---- Calculator Menu ----")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")
    print("5. Exit")

    choice = input("Enter your choice (1-5): ")

    if choice == '5':
        print("Exiting calculator.")
        break

    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))

    match choice:
        case '1':
            print("Result:", add(num1, num2))
        case '2':
            print("Result:", subtract(num1, num2))
        case '3':
            print("Result:", multiply(num1, num2))
        case '4':
            print("Result:", divide(num1, num2))
        case _:
            print("Invalid choice! Please select a valid option.")
