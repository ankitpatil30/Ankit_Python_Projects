# TASK SIX
# GENERATORS, LIST COMPREHENSION AND DECORATORS
# 1. Write a program in Python to find out the character in a string which is uppercase using listcomprehension.
x = 'Justice Comes From Vengeance But That Justice Only Breeds More Vengeance - Nagato Uzumaki'
z = [i for i in x if i.isupper()]
print(z)