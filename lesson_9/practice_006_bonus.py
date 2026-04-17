# Create a program that does the following:
#
# 1. Keeps asking for names, one at a time. Stop asking for names when user's input is "end".
# 2. When the user is done adding names, the program should show two lines for each name:
#    - A line with a greeting: "Hello, {name}!"
#    - A line with the first letter of the user's name: "Your initial is {initial}."
#
# Use at least one function. Extra points if you use two and call a function from another function.
names = []
#str = "Abhishek"
#print(str[:1])


def get_names():
    while True:
        name = input("Please name to add: ")
        if name.lower() == "end":
            break
        names.append(name)

def greet(name):
    print(f"Hello, {name.title()}!")
    print(f"Your Initial is {name[:1].capitalize()}!")

get_names()
for name in names:
    greet(name)