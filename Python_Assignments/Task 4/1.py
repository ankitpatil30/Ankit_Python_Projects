# TASK FOUR
# TRADITIONAL FUNCTIONS,ANONYMOUS FUNCTIONS &
# HIGHER ORDER FUNCTIONS

# 1. Write a program to reverse a string.
# Sample input: “1234abcd”
# Expected output: “dcba4321”

def reverse(a):
    a=a[::-1]
    return a

x=input("Enter a sentence: ")
z=reverse(x)
print(z)