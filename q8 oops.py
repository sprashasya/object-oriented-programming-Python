# Abstract Base Class
# Create an abstract base class Vehicle with an abstract method start_engine. Then, create two derived classes Car and Bike that implement the start_engine method.
# Instantiate the derived class objects and call their start_engine methods.

from abc import ABC,abstractmethod

class Vehicle():
    def __init__(self,name_of_transport):
        self.name_of_transport=name_of_transport
    
    def start_engine(self):
        return "Depends on the Vehicle"

class Bike(Vehicle):
    def __init__(self,name_of_transport):
        self.name_of_transport=name_of_transport
    
    def start_engine(self):
        return "Kickstarting and electrical starting"

class Car(Vehicle):
    def __init__(self,name_of_transport):
        self.name_of_transport=name_of_transport
    
    def start_engine(self):
        return "The starter motor or Self Starter or Self Motor"
    
car1=Car("abcd")
print(car1.start_engine())

bike1=Bike("efgh")
print(bike1.start_engine())

vehicle1=Vehicle("ijkl")
print(vehicle1.start_engine())