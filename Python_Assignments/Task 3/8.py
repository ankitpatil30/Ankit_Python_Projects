#TASK THREE
#DATA STRUCTURES
# 8. Create a new dictionary by concatenating the following two dictionaries: # Sample input:a={1:10,2:20}
# b={3:30,4:40}Expected output: {1:10,2:20,3:30,4:40}
n = int(input("number of key value pairs for dictionary 1: "))
m = int(input("number of key value pairs for dictionary 2: "))
d1 = {}
d2 = {}
print("Enter key value pairs of dictionary 1")
for i in range(1, n+1):
    print("enter key No.", i)
    k = input(": ")
    print("enter value No.", i)
    v = input(": ")
    d1[k] = v

print("\n\n\n\nEnter key value pairs of dictionary 2")
for i in range(1, m+1):
    print("enter key No.", i)
    k = input(": ")
    print("enter value No.", i)
    v = input(": ")
    d1[k] = v

d1.update(d2)
print(d1)