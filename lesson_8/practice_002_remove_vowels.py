# Remove the lowercase vowels in a given string:
str1 = "Hello, World!"

def remove_vowels(str):
    output = ""
    # The vowels are:
    vowels = "aeiou"
    # “y” is not considered a vowel for this task. The input string is always in lowercase.
    # Examples:
    # "hello" --> "hll"
    # "goodbye" --> "gdby"
    for char in str1:
        if char not in vowels:
            output += char
    return output

print(remove_vowels(str1))

