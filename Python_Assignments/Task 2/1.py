#TASK TWO
#OPERATORS AND DECISION MAKING STATEMENT
#1. Write a program in Python to perform the following operation:
#If a number is divisible by 3 it should print “Consultadd” as a string
#If a number is divisible by 5 it should print “Python Training” as a string
#If a number is divisible by both 3 and 5 it should print “Consultadd - Python Training” as a string

x = int(input("enter the number: "))
if x % 5 == 0 and x % 3 == 0:
    print("Consultadd - Python Training")
elif x % 3 == 0:
    print("Consultadd")
elif x % 5 == 0:
    print("Python Training")
else:
    print("number not divisible by 3 or 5")