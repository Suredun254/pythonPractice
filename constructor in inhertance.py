# constructor in inheritance
#

class A:
    def __init__(self):
        print('In A init')

    def feature1(self):
        print('Feature 1')

    def feature2(self):
        print('Feature 2')


# single-level inheritance:
class B(A):
    def __init__(self):
        super().__init__()
        # prints both __init__ of A and B
        print('In B init')

    def feature3(self):
        print('Feature 3')

    def feature4(self):
        print('Feature 4')


class D:
    def __init__(self):
        print('In D init')

    def feature7(self):
        print('Feature 7')

    def feature8(self):
        print('Feature 8')


class E(A, D):
    def __init__(self):
        super().__init__()
        print('In E init')

    def feature9(self):
        print('Feature 9')

    def feature10(self):
        print('Feature 10')


a1 = A()

b1 = B()
# prints init of A and B ; class in inheritance

d1 = D()
e1 = E()
# prints the init of A and E leaving out D , a method referred to as multiple resolution order(MRO)
