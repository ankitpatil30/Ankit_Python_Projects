# EXTRA TASK
# DATA STRUCTURES
# 7. Write a program in python to print the pair of numbers
# whose sum is equal to the result
# number that is let's say 8
# x=[1,2,3,4,5,6,7,8,9,-1]

z = [1, 2, 3, 4, 5, 6, 7, 8, 9, -1]
y = int(input("Enter the result for Number's addition: "))
for i in z:
    for k in z:
        if i+k == y:
            print(i, k)
