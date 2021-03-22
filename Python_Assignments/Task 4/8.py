# TASK FOUR
# TRADITIONAL FUNCTIONS,ANONYMOUS FUNCTIONS &
# HIGHER ORDER FUNCTIONS
# 8. Define a function which can generate and print a tuple where the values are square of numbers
# between 1 and 20 (both 1 and 20 included).

def sq():
    l=[]
    for i in range(1,21):
        i=i**2
        l.append(i)
    return(tuple(l))

print(sq())