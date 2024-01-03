# instance, class and static methods

# ----instance methods-------
# are of two types:
#           1. Accessor methods - used to fetch values i.e get_details
#           2. Mutator methods  - used in changing value i.e set_details
# They work with instance variables within a class
# in defining an instance method it is done as :
# def details(self):
# statements

# ----class methods----
# work with class variables
# must be initialized with @classmethod
# in defining a class method it is done as :
#             @classmethod
# def get_nationality(cls):
# statements

# ----static methods----
# do not work class or instance variables
# must be initialized with @staticmethod
# in defining a class method it is done as :
#             @staticmethod
# def different():
# statements

class Student:
    nationality = 'Kenyan'

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def about_student(self):
        print('{} is {} years old and is a {}'.format(self.name, self.age, Student.nationality))

    def get_age(self):
        print(self.age)

    def set_age(self):
        self.age = 14
        print('the new age for student2 is {}'.format(self.age))

    @classmethod
    def get_nationality(cls):
        return cls.nationality

    @staticmethod
    def different_info():
        print('I love coding')


student1 = Student('Sure', 24)
student2 = Student('Adana', 5)

student1.about_student()
student2.about_student()

student1.get_age()
student2.set_age()

print(Student.nationality)

Student.different_info()
