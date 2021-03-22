# TASK FOUR
# TRADITIONAL FUNCTIONS,ANONYMOUS FUNCTIONS &
# HIGHER ORDER FUNCTIONS
# 12. Write a function to compute 5/0 and use try/except to catch the exceptions

def error():
    z = 5
    q = int(input("Division: 5/x, Enter the value of x: "))
    try:
        x = z/q
        return x
    except ZeroDivisionError:
        return "zero division error"

print(error())