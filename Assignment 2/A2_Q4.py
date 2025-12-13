def prime(num):
    if num<=1:
        return False
    for i in range(2,num):
        if (num%i==0):
            return False
    return True

num=int(input("Enter a number: "))

if prime(num):
    print("The number is prime")
else:
    print("The number is not prime")
    

print("Prime numbers in a given range are: ")
for n in range(2,num):
    if prime(n):
        print(n)   