
text = input("Enter a string: ")

print("First 5 characters:", text[0:5])
print("Characters from index 2 to 6:", text[2:7])

print("From start to index 4:", text[:5])
print("From index 3 to end:", text[3:])

print("Last 4 characters:", text[-4:])
print("String without last 2 characters:", text[:-2])

print("Every second character:", text[::2])
print("Reverse string:", text[::-1])
