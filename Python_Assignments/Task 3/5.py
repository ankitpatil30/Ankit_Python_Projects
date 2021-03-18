#TASK THREE
#DATA STRUCTURES
# 5.Create a new list which contains the specified numbers after removing the even numbers from a predefined list.

list = [11, 44, 33, 22, 55, 88, 66, 77, 99, 121, 154, 132, 110]
specifiedList = []
for i in range(len(list)):
    if list[i] % 2 != 0:
        specifiedList.append(list[i])
        print(list)
        print(specifiedList)
print("The new specified list of numbers: ", specifiedList)

