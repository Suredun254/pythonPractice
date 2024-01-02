# class and object
class Person:

    def __init__(self, age, name):
        self.age = age
        self.name = name

    def details(self):
        print(self.age, self.name)


person1 = Person(15, 'sure')
person2 = Person(16, 'hyne')

# best approach
person1.details()
person2.details()
