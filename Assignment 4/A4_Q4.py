def histogram(num):
    for n in num:
        print(f"{n}:{"*" *n}")
value=list(map(int,input("Enter num: ").split()))
histogram(value)