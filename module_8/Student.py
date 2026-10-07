class Student:
    school_name = "Digital School"

    def __init__(self, name, age, course):
        self.name = name
        self.age = age
        self.course = course

student1=Student(name="Alejna", age=14, course="Python")
student2=Student(name="Yllka", age=17, course="Javascript")
print(student1.school_name)
print(student1.course)
print(student2.course)
