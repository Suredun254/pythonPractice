# class inside a class

class Person:

    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.vehicle = self.Vehicle()

    def get_details(self):
        print(self.name, self.age)
        self.vehicle.get_vehicle_details()

    class Vehicle:
        def __init__(self):
            self.vehicle_name = 'Mercedees'
            self.make = '2023'
            self.wheels = 4

        def get_vehicle_details(self):
            print(self.vehicle_name, self.make, self.wheels)


person1 = Person('Sure', 24)
person2 = Person('Hyne', 20)

person1.get_details()

person2.vehicle.get_vehicle_details()
