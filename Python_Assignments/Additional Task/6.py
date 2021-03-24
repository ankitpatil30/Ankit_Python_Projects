# EXTRA TASK
# DATA STRUCTURES
# 6. Write a program in Python to iterate through
# the string “hello my name is abcde” and print the
# string which is having an even length.

x = "hello my name is abcde"
y =x.split(" ")
print(y)
for i in y:
    if (len(i) % 2 == 0):
        print(i)