def reverse(str):
    return str[::-1]

def vowels(str):
    vowels='aeiouAEIOU'
    count=0
    for ch in str:
        if ch in vowels:
            count+=1
            
    return count        