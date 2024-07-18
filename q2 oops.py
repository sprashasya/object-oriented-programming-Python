# Class Methods and Attributes:
# Add a method named display_student to the Student class that prints the student's details. Instantiate a few Student objects and call this method.

class Student():
    def __init__(self,name,age,grade):
        self.name=name
        self.age=age
        self.grade=grade
    
    def display_student(self):
        return f"{self.name}  {self.age}  {self.grade}"
    
student_one=Student("Abcd",18,"A+")
print(student_one.display_student())

student_two = Student("Efgh",22,"B")
print(student_two.display_student())
