#TASK TWO
#OPERATORS AND DECISION MAKING STATEMENT
#6. What is the output of the following code examples?
x=123
for i in x:
 print(i)

Output: Type Error: x is not iterable

i = 0
while i < 5:
print(i)
i += 1
if i == 3:
break
else:
print(“error”)

Output:
0
error
1
error
2


count = 0
while True:
 print(count)
 count += 1
 if count >= 5:
  Break

Output: NameError: Break is not defined
if it was "break" instead of "Break" then:
0
1
2
3
4