# TASK FOUR
# TRADITIONAL FUNCTIONS,ANONYMOUS FUNCTIONS &
# HIGHER ORDER FUNCTIONS
# 7. Define a function that can accept two strings as input and print the string with the maximum length
# in the console. If two strings have the same length, then the function should print both the strings line by line.


def max_len(q, w):
    if len(q)>len(w):
        return q
    elif len(w)>len(q):
        return w
    elif len(q)==len(w):
        return (q + '\n' + w)

x = input("Enter first string: ")
z = input("Enter second string: ")
print("The results: ", max_len(x, z))