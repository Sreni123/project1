class Student:
    def __init__(self,name,age):
        self.name=name
        self.age=age

    def display(self):
        print("Student name:",self.name)
        print("Student age:",self.age)
s1=Student("sreni",21)
s2=Student("sreni",21)
s1.display()
s2.display()
