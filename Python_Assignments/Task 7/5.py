# TASK SEVEN
# CLASSES AND OBJECTS
# 5. Write a Person class with an instance variable “age” and a constructor that takes an integer as aparameter.
# The constructor must assign the integer value tothe age variable after confirming theargument passed is not negative;
# if a negative argument is passed then the constructor should set age to 0 and print “Age is not valid, setting age to 0”.
# In addition, you must write the following instance methods
# * yearPasses() should increase age by the integer value that you are passing inside the function.
# * amIOld() should perform the following conditional actions:
#     #If age is between 0 and <13, print “You are young”.
#     #If age is >=13 and <=19 , print “You are a teenager”.
#     #Otherwise, print “You are old”.

# Sample Input for amIOld():
#     -1 
#     4
#     1
#     0
#     1
#     6
#     1
#     8
#     6
#     4
#     3
#     8
# Expected Output for amIOld():
#     Age is not valid, setting age to 0.
#     You are young.
#     You are young.
#     You are a teenager.
#     You are a teenager.
#     You are old.
#     You are old.
# Consider the age variable to be set to 38 then:
# Sample Input for yearPasses(): 4
# Expected Output for yearPasses(): 42


class Person:
    age = 0
    def __init__(self,initialAge):
        # Add some more code to run some checks on initialAge
        if initialAge < 0:
            print("Age is not valid, setting age to 0.")
        else:
            self.age = initialAge
    def amIOld(self):
        # Do some computations in here and print out the correct statement to the console
        if self.age < 13:
            print("You are young.")
        elif self.age >= 13 and self.age < 18:
            print("You are a teenager.")
        else:
            print("You are old.")
    def yearPasses(self, sample):
        # Increment the age of the person in here
        print("After", sample,"years: ",self.age+sample)

x = int(input("Number of age inputs: "))
for i in range(1, x+1):
    a = int(input("Enter age: "))
    m = Person(a)
    m.yearPasses(4)
    m.amIOld()
