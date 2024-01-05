# method overloading under polymorphism

class Student:
    def __init__(self, m1, m2):
        self.m1 = m1
        self.m2 = m2

    def sum(self, a=None, b=None, c=None):

        s = 0

        if a != None and b != None and c != None:
            s = a + b + c
        elif a != None and b != None:
            s = a + b
        else:
            s = a
        return s


student1 = Student(59, 70)

sum1 = student1.sum(40, 60, 90)
print('sum 1 is ', sum1)

sum1 = student1.sum(40, 60)
print('sum 2 is ', sum1)

sum1 = student1.sum(40, )
print('sum 3 is ', sum1)
