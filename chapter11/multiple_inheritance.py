# Parent class 1
class Student:
    def study(self):
        return "I am studying"

# Parent class 2  
class Athlete:
    def play(self):
        return "I am playing sports"

# Child class inheriting from both
class StudentAthlete(Student, Athlete):
    def hobby(self):
        return "I both study and play!"

# Usage
sa = StudentAthlete()
print(sa.study())  # I am studying
print(sa.play())   # I am playing sports
print(sa.hobby())  # I both study and play!