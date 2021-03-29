# TASK SEVEN
# CLASSES AND OBJECTS

# 1. Write a program that calculates and prints the value according to
# the given formula:Q= Square root of [(2*C*D)/H]
# Following are the fixed values of C and H:
# C is 50.
# H is 30.
# D is a variable whose values should be input to your program in a comma-separated sequence.

import math

n = input("Provide the values of D: ")
n = n.split(',')

result = []
for D in n:
    Q = math.sqrt(2 * 50 * int(D) / 30)
    result.append(Q)

print(result)