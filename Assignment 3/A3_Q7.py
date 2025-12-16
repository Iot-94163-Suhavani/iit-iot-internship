
def factorial(n):
    if n == 0 or n == 1:    
        return 1
    else:
        return n * factorial(n - 1)

def power(base, exp):
    if exp == 0:            
        return 1
    else:
        return base * power(base, exp - 1)

num = int(input("Enter a number for factorial: "))
base = int(input("Enter base: "))
exponent = int(input("Enter exponent: "))

print("Factorial of", num, "is:", factorial(num))
print(base, "raised to power", exponent, "is:", power(base, exponent))
