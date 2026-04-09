# Given an integer, return the integer with reversed digits.
#
# Note:
# The integer could be either positive or negative.
#
# Example:
# -876 -> -678
def reverse_an_integer(a):
    if a >= 0:
        return int(str(a)[::-1])
    else:
        return -1 * int(str(abs(a))[::-1])

print(reverse_an_integer(106))
print(reverse_an_integer(-106))