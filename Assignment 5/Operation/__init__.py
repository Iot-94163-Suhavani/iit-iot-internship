import arithmetic
import string_ops

a=int(input("Enter number 1: "))
b=int(input("Enter number 2: "))
print("Addition: ",arithmetic.add(a,b))
print("Multiplication: ",arithmetic.mult(a,b))

str=input("Enter a string: ")
print("Reversed string: ",string_ops.reverse(str))
print("Number of vowels in string: ",string_ops.vowels(str))