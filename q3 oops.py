# Inheritance:
# Create a base class Animal with attributes name and species, and a method make_sound that prints a general message. Then, create two derived classes Dog and Cat that inherit from Animal and override the make_sound method to print a specific sound for each animal.

class Animal():
    def __init__(self,name,species):
        self.name=name
        self.species=species
    
    def make_sound(self):
        return "Animal Sound"


class Dog(Animal):
    def __init__(self,name,species):
        super().__init__(name,species)
    
    def make_sound(self):
        return "Barking"


class Cat(Animal):
    def __init__(self,name,species):
        super().__init__(name,species)
    
    def make_sound(self):
        return "meows"

animal_one=Animal("Birds","Wood duck")
print(animal_one.make_sound())
print(animal_one.name)
print(animal_one.species)

animal_two=Dog("Dog","German Shepherd")
print(animal_two.make_sound())
print(animal_two.name)
print(animal_two.species)
print(isinstance(animal_two,Animal))

animal_three=Cat("Cat","British Shorthair")
print(animal_three.make_sound())
print(animal_three.name)
print(animal_three.species)
print(isinstance(animal_three,Animal))