# The Fibonacci sequence is a series of numbers where each number is the sum of the two preceding ones.
# Print out the Fibonacci sequence until the given n-th in the sequence.
# Example: n = 7,
# Print out the sequence: 0, 1, 1, 2, 3, 5, 8
n = 7
o_list = []
n1 = 0
n2 = 1
o_list.append(n1)
for i in range(1, n):
    o_list.append(n2)
    n3 = n1 + n2
    n1 = n2
    n2 = n3

print(o_list)
