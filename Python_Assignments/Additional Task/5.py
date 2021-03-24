# EXTRA TASK
# DATA STRUCTURES
# 5. Write a program in Python to reverse a string and 
# print only the vowel alphabet if it exists in the
# string with their index.

x = input("Enter the String: ")

y = x[::-1]
print("Reversed String: ", y)
vow = ['a','e','i','o','u','A','E','I','O','U']

print("Only Vowels: ")
for i in range(len(y)):
	if y[i] in vow:
		print(y[i], i)
