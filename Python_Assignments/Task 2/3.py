#TASK TWO
#OPERATORS AND DECISION MAKING STATEMENT
#3. Write a program in Python to implement the given flowchart:

a, b, c = 10, 20, 30
avg = (a + b + c) / 3
print("Avg =  ", avg)

if avg > a and avg > b and avg > c:
    print("Avg higher than a, b, c")
elif avg > a and avg > b:
        print("Avg higher than a, b")
elif avg > a and avg > c:
        print("Avg higher than a, c")
elif avg > b and avg > c:
        print("Avg higher than b, c")
elif avg > a:
        print("Avg only higher than a")
elif avg > b:
        print("Avg is just higher than b")
elif avg > c:
        print("Avg is just higher than c")