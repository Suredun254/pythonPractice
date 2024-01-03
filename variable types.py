# instance and class variables

# class variables are defined outside the __init__
# instance variables are defined within the init

# to change a class variable outside class statements do
# class.variable_name=value

class Student:
    nationality = 'Kenyan'

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def about_student(self):
        print('{} is {} years old and is a {}'.format(self.name, self.age, Student.nationality))


student1 = Student('Sure', 24)
student2 = Student('Adana', 5)

student1.about_student()
student2.about_student()

Student.nationality = 'Ugandan'

print('{} is now a {}'.format(student1.name, Student.nationality))
print('{} is now a {}'.format(student2.name, Student.nationality))
