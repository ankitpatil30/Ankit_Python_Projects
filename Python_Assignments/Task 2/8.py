#TASK TWO
#OPERATORS AND DECISION MAKING STATEMENT
#8. Write a program that accepts a string as an input from the user and calculate the number of digits and letters.
#Sample input: consul72
#Expected output: Letters 6 Digits 2

ltrs = 0
dgts = 0
strg = input("Enter the sentence: ")
for x in strg:
    if x.isalpha():
        ltrs += 1
    elif x.isdigit():
        dgts += 1
    elif x == " ":
        continue
    else:
        print("wrong input")
print("Letters:", ltrs)
print("Digits:", dgts)