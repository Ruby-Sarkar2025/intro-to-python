# Create a variable called number. Set it to any number.

# Convert the number to negative and print it.
# Keep the number as is, if the number is already negative.

# 5 => -5
# -1 => -1
def convert_to_negative(number):
    if number < 0:
        return number
    else:
        return number * -1


a = -15
print(convert_to_negative(a))



