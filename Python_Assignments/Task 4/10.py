# TASK FOUR
# TRADITIONAL FUNCTIONS,ANONYMOUS FUNCTIONS &
# HIGHER ORDER FUNCTIONS
# 10. Write a program which uses filter() to make a list whose elements are even numbers between 1
# and 20 (both included)
result = filter(lambda x: x % 2 == 0, range(1, 21))
print(list(result))
