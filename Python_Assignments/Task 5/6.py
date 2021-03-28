# TASK FIVE
# FILE HANDLING AND EXCEPTION HANDLING
# 6.Read doc.txt file using Python File handling concept and return only the even length string fromthe file.
# Consider the content of doc.txt as given below:
# Hello I am a file
# Where you need to return the data string
# Which is of even length
# Make sure you return the content in The same link as it is present.

a = open('doc.txt', 'w')
a.write("Hello I am a file\nWhere you need to return the data string\nWhich is of even length\nMake sure you return the content in The same link as it is present.")
a.close()
b = open('doc.txt', 'r')
x = b.read()
y = {i:x[i] for i in range(len(x)) if i%2==0 }
print(y)
# for i in range(len(x)):
#     if i%2 == 0:
#         print(i, x[i])
b.close()