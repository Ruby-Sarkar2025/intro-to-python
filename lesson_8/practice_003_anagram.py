# Given two words, check if both are anagrams.
# An anagram of a string is another string that contains the same characters, only the order
# of characters can be different.
# For example:
# is_anagram('cat', 'act') => should return True
# is_anagram('bus', 'sub') => should return True
# is_anagram('map', 'cap') => should return False

def is_anagram(str1, str2):
    if len(str1) != len(str2):
        return False
    str1 = str1.lower()
    str2 = str2.lower()
    for char in str1:
        if str1.count(char) != str2.count(char):
            return False
    return True

print(is_anagram("cat", "act"))
print(is_anagram("bus", "sub"))
print(is_anagram("map", "cap"))
