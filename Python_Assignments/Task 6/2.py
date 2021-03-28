# TASK SIX
# GENERATORS, LIST COMPREHENSION AND DECORATORS

# 2.Write a program to construct a dictionary from the two lists containing the names of students and their corresponding subjects.
# The dictionary should map the students with their respective subjects.
# Let’s see how to do this using for loops and dictionary comprehension.
#     HINT- Use Zip function alsoSample input: students = ['Smit', 'Jaya', 'Rayyan']
#     subjects = ['CSE', 'Networking', 'Operating System']
#     Expected output: {‘Smit’ : ’CSE’ , ’Jaya’ : ’Networking’ , ’Rayyan’ : ’Operating System’}

st = ['Matt','Naruto','Yamato','Kakashi','Sasuke','Nagato','Shikamaru']
sb = ['Computer Sceince','WindStyle','EarthStyle','LighteningStyle','LighteningStyle','Rinnegan','ShadowStyle']

print(dict(zip(st,sb)))
print({st[i]:sb[i] for i in range(len(st))})
