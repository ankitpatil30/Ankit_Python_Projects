# TASK FIVE
# FILE HANDLING AND EXCEPTION HANDLING
# 1. Write a program in Python to allow the error of syntax to be handled using exception handling.
# HINT: Use SyntaxError

try:
    eval('x===x')
except SyntaxError:
    print("You cannot do that")

