# Given a list.
# Calculate sum and multiplication of all elements.
# Print the list, sum and multiplication of elements.
# For example:
Input = [1, 2, 3, 4]
# Output sum: 10
# Output multiplication: 24

def sum_multiplication(numbers):
    sum = 0
    multiplier = 1
    for i in Input:
        sum = sum + int(i)
        multiplier = multiplier * int(i)

    return sum, multiplier

sum, multiplier = sum_multiplication(Input)

print(sum)
print(multiplier)



