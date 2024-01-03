# inheritance in python
# single-level, multi-level and multiple inhertance

class A:
    def feature1(self):
        print('Feature 1')

    def feature2(self):
        print('Feature 2')


# single-level inheritance:
class B(A):
    def feature3(self):
        print('Feature 3')

    def feature4(self):
        print('Feature 4')


# multilevel inheritance
class C(B):
    def feature5(self):
        print('Feature 5')

    def feature6(self):
        print('Feature 6')


class D:
    def feature7(self):
        print('Feature 7')

    def feature8(self):
        print('Feature 8')


# multiple inheritance
class E(A, D):
    def feature9(self):
        print('Feature 9')

    def feature10(self):
        print('Feature 10')


a1 = A()
b1 = B()
c1 = C()
d1 = D()
e1 = E()

a1.feature2()
b1.feature1()
c1.feature1()
e1.feature1()
