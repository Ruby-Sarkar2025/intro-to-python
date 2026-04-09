# The [::-1] slicing syntax starts from the end of the string
# (index -1) and goes backward with a step of -1, effectively
# reversing the string.

def reverse_string(s):
    return s[::-1]

print(reverse_string("hello"))
print(reverse_string("world"))