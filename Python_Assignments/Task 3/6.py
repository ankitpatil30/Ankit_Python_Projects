#TASK THREE
#DATA STRUCTURES
# 6. Create a list of elements such that it contains the squares of the first and last 5 elements between 1 and 30 (both included).

list = []

for i in range(1, 31):
    if i >= 1 and i <= 5:
        list.append(i**2)
    if i >= 26 and i <= 30:
        list.append(i**2)
print("the squares of the first and last 5 elements between 1 and 30 (both included):", list)


