# EXTRA TASK
# DATA STRUCTURES
# 9. Write a program to find out the occurrence of a specific character from an alphanumeric string.
# Sample input: 12abcbacbaba344ab
# Expected output: a=5 b=5 c=2
# NOTE: Make sure to avoid counting the occurrence of numeric values in the string.

mystr = input("Enter the string to count number of occurences: ")

str = {x: mystr.count(x) for x in mystr if x.isdigit() == False}
print("the occurrences of all the characters: ",str)
