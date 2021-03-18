#TASK THREE
#DATA STRUCTURES
# 7. Write a program to replace the last element in a list with another list.Sample input: [1,3,5,7,9,10],
# [2,4,6,8]Expected output: [1,3,5,7,9,2,4,6,8]

a = list(map(int,input("Enter the numbers for list 1: ").strip().split(",")))
b = list(map(int,input("Enter the numbers for list 2: ").strip().split(",")))
a.remove(a[-1])
a.extend(b)
print(a)


