# Class Variables vs Instance Variables:
# Create a class Car with instance variables color and model, and a class variable number_of_wheels set to 4. Instantiate a few Car objects and demonstrate the difference between class variables and instance variables.


class Car():
    number_of_wheels=4

    def __init__(self,color,model):
        self.color=color
        self.model=model


c1=Car("blue","abc")
print(c1.model)
print(c1.color)
print(Car.number_of_wheels)