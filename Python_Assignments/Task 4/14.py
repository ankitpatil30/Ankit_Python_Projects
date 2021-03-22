# TASK FOUR
# TRADITIONAL FUNCTIONS,ANONYMOUS FUNCTIONS &
# HIGHER ORDER FUNCTIONS
# 14. Write a program in Python to find the values which are not divisible by 3 but are a multiple of 7.
# Make sure to use only higher order functions.

x = int(input("Enter the number n for values from 1 to n : "))
y = filter(lambda x:x%3!=0 and x%7==0, range(1,x+1))
print(list(y))