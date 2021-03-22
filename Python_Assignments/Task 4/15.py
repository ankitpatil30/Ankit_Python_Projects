# TASK FOUR
# TRADITIONAL FUNCTIONS,ANONYMOUS FUNCTIONS &
# HIGHER ORDER FUNCTIONS
# 15. Write a program in Python to multiply the elements of a list by itself using a traditional function
# and pass the function to map() to complete the operation.

def mult(dh):
    return dh * dh

x = [1,22,10,30,543,999,80,76,7,5,4,3]
y = map(mult, x)
print(list(y))