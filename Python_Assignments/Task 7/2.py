# TASK SEVEN
# CLASSES AND OBJECTS
# 2. Define a class named Shape and its subclass Square. The Square class has
# an init function whichtakes length as argument. Both classes have an area function
# which can print the area of the shape where Shape’s area is 0 by default.



class Shape:
    def __init__(self):
        pass

    def area(self):
        return 0

class Square(Shape):
    def __init__(self, l):
        print("Area of Shape: ", Shape.area(self))
        self.length = l

    def area(self):
        print("Area of Sqaure: ")
        return self.length*self.length

a = Square(20)
b = Shape()
print(a.area())
print(b.area())