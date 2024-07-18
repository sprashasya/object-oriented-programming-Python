# Polymorphism:
# Create a base class Shape with a method area. Then, create derived classes Rectangle and Circle that override the area method to calculate the area of a rectangle and a circle, respectively. Create a function that takes a Shape object and prints its area.

import math 

class Shape():
    def __init__(self,shapename):
        self.shapename=shapename
    
    def area(self):
        return "area"

class Rectangle(Shape):
    def __init__(self,shapename,Length,Breadth):
        super().__init__(shapename)
        self.Length=Length
        self.Breadth=Breadth
    
    def area(self):
        return self.Length*self.Breadth
    
class Circle(Shape):
    def __init__(self,shapename,Radius):
        super().__init__(shapename)
        self.Radius=Radius
        
    def area(self):
        return math.pi*(self.Radius**2)
    
shape1=Shape("rhombus")
print(shape1.area)
print(shape1.shapename)

shape2=Rectangle("Rectangle",2,2)
print(shape2.shapename)
print(shape2.Length)
print(shape2.Breadth)
print(shape2.area())

shape3=Circle("Circle",2)
print(shape3.shapename)
print(shape3.Radius)
print(shape3.area())