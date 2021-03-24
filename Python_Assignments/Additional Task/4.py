# EXTRA TASK
# DATA STRUCTURES
# 4. Write a program in Python to iterate through the list of 
# numbers in the range of 1,100 and print
# the number which is divisible by 3 and is a multiple of 2.

for i in range(1,100):
	if (i%3 == 0 & i%2 ==0):
		print(i)
	else:
		continue
