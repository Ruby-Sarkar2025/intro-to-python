# A palindrome is a word, number, phrase, or other sequence of symbols
# that reads the same backwards as forwards:
#
# madam -> madam
# racecar -> racecar
# tacocat -> tacocat
#
# Write a program that will print True if the word is a palindrome
# and False if it is not.

def check_palindrome(s):
    if s == s[::-1]:
        return "Palindrome"
    else:
        return "Not Palindrome"

print(check_palindrome("hello"))
print(check_palindrome("madam"))