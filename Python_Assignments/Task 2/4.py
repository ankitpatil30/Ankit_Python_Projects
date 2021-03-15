#TASK TWO
#OPERATORS AND DECISION MAKING STATEMENT
#4. Write a program in Python to break and continue if the following cases occurs:
#If user enters a negative number just break the loop and print “It’s Over”
#If user enters a positive number just continue in the loop and print “Good Going”

x = int(input("Enter a number: "))
while True:
    if x < 0:
        print("It's over")
        break
    else:
        print("Good Going")
        x = int(input("Enter a number: "))