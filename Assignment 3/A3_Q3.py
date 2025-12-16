# Function to count vowels
def count_vowels(text):
    vowels = "aeiouAEIOU"
    count = 0
    for ch in text:
        if ch in vowels:
            count += 1
    return count

def count_consonants(text):
    vowels = "aeiouAEIOU"
    count = 0
    for ch in text:
        if ch.isalpha() and ch not in vowels:
            count += 1
    return count

def vowel_consonant_ratio(vowels, consonants):
    if consonants == 0:
        return "Undefined (no consonants)"
    return vowels / consonants

string = input("Enter a string: ")

vowel_count = count_vowels(string)
consonant_count = count_consonants(string)
ratio = vowel_consonant_ratio(vowel_count, consonant_count)

print("Number of vowels:", vowel_count)
print("Number of consonants:", consonant_count)
print("Ratio of vowels to consonants:", ratio)


