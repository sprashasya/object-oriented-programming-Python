# Class and Object Creation:
# Create a class named Student with attributes like name, age, and grade. Then, create an object of this class and print the details of the student.

class Student():
    def __init__(self,name,age,grade):
        self.name = name
        self.age = age
        self.grade=grade

student_one = Student("Abcd",18,"A+")
print(student_one.name)
print(student_one.age)
print(student_one.grade)

student_two = Student("Efgh",22,"B")
print(student_two.name)
print(student_two.age)
print(student_two.grade)