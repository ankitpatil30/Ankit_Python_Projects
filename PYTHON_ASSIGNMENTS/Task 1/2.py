#TASK ONE NUMBERS AND VARIABLES
#2. Create a variable of type complex and swap it with another variable of type integer

a = 10+20j
b = 2
print('a = ',a ,'b = ', b)
print(type(a), type(b))
x = a
a = b
b = x
print('a = ',a ,'b = ', b)
print(type(a), type(b))