# Homework Lesson 5 - Workshop - Homework

# READ CAREFULLY THE EXERCISE DESCRIPTION AND SOLVE IT RIGHT AFTER IT

# Challenge 1
# Make a number Positive
#
# Create a variable called my_number and set it to any integer value.
# Write code to make the number positive if it's negative, and keep it
# as is if it's already positive or zero.
#
# Example:
# Input: -3 => Output: 3
# Input: 5 => Output: 5

def make_positive( my_number ):
    if my_number > 0:
        return my_number
    else:
        return abs(my_number)

#print(make_positive(-1210))


# ---------------------------------------------------------------------

# Challenge 2
# BinGo!
#
# If the number is divisible of 3, print “Bin”
# If the number is divisible of 7, print “Go”
# For numbers which are divisible of 3 and 7, print “BinGo”
# Otherwise, print the original number: “{number} is just a number”
def bingo(a):
    if a % 3 == 0 and a % 7 == 0:
        str = "Bingo"
    elif a % 3 == 0:
        str = "Bin"
    elif a % 7 == 0:
        str = "go"
    else:
        str = f"{a} is just a number"
    return str

#print(bingo(10))

# ---------------------------------------------------------------------

# Challenge 3
# Find the middle number
#
# Given three different numbers x, y, and z, find the number that is neither
# the smallest nor the largest and print it.
#
# Example:
# x = 1, y = 5, z = 3 => Output: 3
def guess_middle(a, b, c):
    if (a - b) * (c - a) > 0: #assume a is the middle
        return a
    elif (b - a) * (c - b) > 0: #assume b is the middle
        return b
    else:
        return c

#print(guess_middle(11, 16, 7))
# ---------------------------------------------------------------------

# Challenge 4
# Palindrome Numbers
#
# Ask a user to input a number.
# Write a program to check if the given number is a palindrome.
# It should print True if the number is a palindrome and False if it is not.
#
# Palindrome number: 121, 898

def check_palindrome(num):
    a = str(num)
    b = a[::-1]
    if a == b:
        return True
    else:
        return False

#print(check_palindrome(665))
#print(check_palindrome(666))

# ---------------------------------------------------------------------

# Challenge 5
# Reverse a string
#
# You're part of a team working on analyzing customer reviews for a new video game.
# Due to a software glitch, some reviews have been recorded in reverse with punctuation
# at the beginning instead of the end. Your task is to correct these reviews so that they
# are in the correct order and the punctuation is appropriately placed at the end of the
# sentence or word.
#
# Example: "tcefreP!" -> Perfect!

def reverse(sample):
    return sample[::-1]

#print(reverse("hello world"))