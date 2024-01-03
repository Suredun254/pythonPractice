class Student:
    def __init__(self, mark1, mark2):
        self.mark1 = mark1
        self.mark2 = mark2

    def __add__(self, other):
        mark1 = self.mark1 + other.mark1
        mark2 = self.mark2 + other.mark2
        mark3 = Student(mark1, mark2)

        return mark3

    def __gt__(self, other):
        r1 = self.mark1 + self.mark2
        r2 = other.mark1 + other.mark2

        if r1 > r2:
            return True
        else:
            return False

    def __str__(self):
        return self.mark1, self.mark2


student1 = Student(50, 70)
student2 = Student(60, 80)

mark3 = student1 + student2
print(mark3.mark1 + mark3.mark2)

if student1 > student2:
    print('student 1 leads')
else:
    print('Student 2 leads ')

print(student1.__str__())
