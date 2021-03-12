#TASK ONE NUMBERS AND VARIABLES
#3. Swap two numbers using a third variable and do the same task without using any third variable.
print('using third variable: ')
a = 10
b = 20
print('a = ',a ,'b = ', b)
x = a
a = b
b = x
print('a = ',a ,'b = ', b)

print('without using third variable: ')
a = 10
b = 20
print('a = ',a ,'b = ', b)
a,b = b,a
print('a = ',a ,'b = ', b)