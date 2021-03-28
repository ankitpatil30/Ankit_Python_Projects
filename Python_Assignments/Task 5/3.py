# TASK FIVE
# FILE HANDLING AND EXCEPTION HANDLING
# 3.Write a program to handle an error if the user entered a number more than four digits
# it should return “The length is too short/long !!! Please provide only four digits”
a=1
while a==1:
    try:
        n = int(input("Enter the 4 digit number : "))
        print(n)
        if n > 9999 or n < 1000:
            a = 1
            raise
        else:
            a = 2
    except:
        print("The length is too short/long !!! Please provide only four digits")