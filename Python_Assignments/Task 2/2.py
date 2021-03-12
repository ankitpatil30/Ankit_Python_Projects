#TASK TWO
#OPERATORS AND DECISION MAKING STATEMENT
#2. Write a program in Python to perform the following operator based task:
#Ask user to choose the following option first:
#If User Enter 1 - Addition
#If User Enter 2 - Subtraction
#If User Enter 3 - Division
#If User Enter 4 - Multiplication
#If User Enter 5 - Average
#Ask user to enter two numbers and keep those numbers in variables num1 and num2
#respectively for the first 4 options mentioned above.
#Ask the user to enter two more numbers as first and second for calculating the average as
# soon as the user chooses an option 5.
#At the end if the answer of any operation is Negative print a statement saying “NEGATIVE”
#NOTE: At a time a user can only perform one action.

x = int(input("choose the following option:\nEnter 1 - Addition\nEnter 2 - Subtraction\nEnter 3 - Division\n"
                       "Enter 4 - Multiplication\nEnter 5 - Average\nEnter the Option: "))

num1 = int(input("Enter first number: "))
num2 = int(input("Enter a second number: "))
if x == 5:
    first = int(input("Enter third number: "))
    second = int(input("Enter fourth number: "))
else:
    pass

if x == 1:
    result = num1 + num2
elif x == 2:
    result = num1 - num2
elif x == 3:
    result = num1 / num2
elif x == 4:
    result = num1 * num2
elif x == 5:
    result = (num1 + num2 + first + second) / 4
else:
    print("Incorrect Option")

if result < 0:
    print("NEGATIVE")
else:
    print(result)