#TASK TWO
#OPERATORS AND DECISION MAKING STATEMENT
#5. Write a program in Python which will find all such numbers which are divisible by 7 but are not a
#multiple of 5, between 2000 and 3200.

for x in range(2000, 3200):
    if (x % 7 == 0) and (x % 5 != 0):
        print(x)