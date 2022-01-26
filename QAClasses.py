#QA tutorial

class Student:

    def __init__(self, name, age):
        self.name = name
        self.age = age

John = Student("John", "21")
Jane = Student("Jane", "22")

print(getattr(John,"age"))

#QA exercise

# In a new Python file, create a class of students.
# It should contain the following attributes: name, age, and class with default value "student".
# It should also contain a method which takes in 3 test scores and prints the students average test score.

class Students:
    def __init__(self, name = "Student", age = "Student", Class = "Student"):
        self.name = name
        self.age = age
        self.Class = Class

    def AVGTestScore(ins1,ins2,ins3):
        total = round(int(ins1 + ins2 + ins3) /3)
        return total

Jon = Students()
Jonny = Students("Jonny", "22", "IT")
print(Jonny.Class)
print(Jon.Class)

score1 = int(input("Please enter the student score: "))
score2 = int(input("Please enter the student score: "))
score3 = int(input("Please enter the student score: "))

print (Students.AVGTestScore(score1, score2, score3))

