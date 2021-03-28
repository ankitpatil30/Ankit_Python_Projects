# TASK SIX
# GENERATORS, LIST COMPREHENSION AND DECORATORS
# 4.Write a program in Python using generators to reverse the string.Input String = “Consultadd Training”

def rev(s):
    yield s[::-1]

str = "Consultadd Training"
x= rev(str)
print(next(x))