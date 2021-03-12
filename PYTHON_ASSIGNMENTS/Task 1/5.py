#TASK ONE NUMBERS AND VARIABLES
#5. Write a program to complete the task given below:
#Ask users to enter any 2 numbers in between 1-10 , add the two numbers and keep the sum in
#another variable called z. Add 30 to z and store the output in variable result and print result as the
#final output

x, y = input('enter any 2 numbers in between 1-10: ').split(' ')
z = int(x) + int(y)
result = z + 30
print('Final Output: ', result)