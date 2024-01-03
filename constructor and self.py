# Constructor and self
# updating and comparing of objects
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def details(self):
        print('{} is {} years old'.format(self.name, self.age))

    def update(self) -> object:
        self.age = 40

    def compare(self, person2):

        if self.age == person2.age:
            return True
        else:
            return False


person1 = Person('sure', 30)
person2 = Person('hyne', 18)

person1.details()
person2.details()

# to update details
person1.update()
print(person1.age)

# to compare the two values

if person1.compare(person2):
    print('they share the same age')

else:
    print('their ages are different')
