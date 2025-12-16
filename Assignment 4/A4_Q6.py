#prices = [105, 110, 108, 112, 115, 116, 114]
prices=list(map(int,input("Enter list :").split()))
for i in range(len(prices) - 2):
    avg = sum(prices[i:i+3]) / 3
    print(round(avg, 2))