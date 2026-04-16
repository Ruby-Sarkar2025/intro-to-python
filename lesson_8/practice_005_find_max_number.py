# Your goal is to write a Python program that finds the maximum number in a given list of numbers.
# Example:
def max_number(numbers):
    # Output : 99
    Output = 0
    for n in numbers:
        if n > Output:
            Output = n
    return Output

numbers = [1, 2, 42, 77, 99, -100]
print(max_number(numbers))
