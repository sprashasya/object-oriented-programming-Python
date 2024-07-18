# Encapsulation:
# Modify the Student class to make the age attribute private. Add getter and setter methods for the age attribute to ensure it can be accessed and modified only through these methods.

class Student():
    def __init__(self,name,age,grade):
        self.name=name
        self.__age=age
        self.grade=grade

    def get_age(self):
        return self.__age
    
    def set_age(self,setage):
        self.__age=setage
    
    def display_student(self):
        return f"{self.name}  {self.__age}  {self.grade}"

student_one = Student("Abcd",18,"A+")
print(student_one.name)
print(student_one.get_age())
print(student_one.grade)
student_one.set_age(20)
print(student_one.get_age())