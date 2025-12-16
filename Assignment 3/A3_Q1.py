
text = "   Sun Beam  "

print(text.strip())

print(text.capitalize())

print(text.count("1"))

print(text.endswith("World  "))

print(text.startswith("   He"))

print(text.find("Beam"))

print(text.istitle())

print(text.upper())

num = "123"
print(num.isdecimal())

print(text.removeprefix("S"))

print(text.replace("Beam", "Rise"))

print(text.split())

translation_table = str.maketrans("nm", "NM")
print(text.translate(translation_table))
