# EXTRA TASK
# DATA STRUCTURES
# 8. Write a program in Python to complete the following task:
# Create two lists such as even_list and odd_list
# Ask user to enter a number in the range of 1,50 and make sure if the entered number is 
# even, append it to the even_list and if the entered number is odd append it to the odd_list.
# Keep that in mind you can only add 5 items in each list
# Make sure once you enter all the 5 elements, calculate the sum of the list and return the
# maximum of the list.

even_list = []
odd_list = []
x = int(input("Enter a number in the range of 1,50 (only 5 even and 5 odd): "))

while len(even_list) < 5 or len(odd_list) < 5:
    if x >= 1 and x <= 50:
        if (x%2 == 0 and len(even_list) < 5):
            even_list.append(x)
            print("Even List", even_list)
        elif (x%2 == 1 and len(odd_list) < 5):
            odd_list.append(x)
            print("Odd List", odd_list)
        elif (len(even_list) == 5):
            print("even list is full")
        elif (len(odd_list) == 5):
            print("odd list is full")
        else:
            break
    x = int(input("Enter a number in the range of 1,50 (only 5 even and 5 odd): "))

print("Even List: ", even_list, "\nOdd List: ", odd_list)
print("Sum of Even List: ", sum(even_list))
print("Max of Even List: ", max(even_list))
print("Sum of odd List: ", sum(odd_list))
print("Max of odd List: ", max(odd_list))