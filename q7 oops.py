# Method Overloading (using default arguments):
# Create a class Calculator with a method add that can take either two or three arguments and returns their sum. Demonstrate method overloading using default arguments in Python.

class Calculator():
        def __init__(self,brand):
              self.brand=brand
        
        def add(self,a,b,c=0):
            return a+b+c

a=Calculator("casio")
print(a.calculator)
print(a.add(3,4))
