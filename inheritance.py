"""Class inheritance is a very useful Object-oriented Programming construct for sharing and reusing code. 
Inheritance makes it possible to break up and organize your code into a hierarchy, from generic to specific.
Objects that belong to classes that are higher up in the hierarchy (more generic) are accessible by subclasses, but not vice versa."""

class Vehicle:

    def __init__(self, make, model, fuel="gas"):
        self.make = make
        self.model = model
        self.fuel = fuel


class Car(Vehicle):

    def __init__(self, make, model, fuel="gas"):
        super().__init__(make, model, fuel)



my_car = Car("Ford", "Thunderbird")
print(f"my_car is type {type(my_car)}")
print(f"my_car uses {my_car.fuel}")

print(f"my_car is a Car: {isinstance(my_car, Car)}")
print(f"my_car is a Vehicle: {isinstance(my_car, Vehicle)}")
print(f"Car is a subclass of Vehicle: {issubclass(Car, Vehicle)}")


# We can use a subclass to override variables that belong to a parent class.

# vehicle.py

class Vehicle:
    number_of_wheels = 4

    def __init__(self, make, model, fuel="gas"):
        self.make = make
        self.model = model
        self.fuel = fuel

class Car(Vehicle):

    def __init__(self, make, model, fuel="gas"):
        super().__init__(make, model, fuel)

class Truck(Vehicle):
    number_of_wheels = 6

    def __init__(self, make, model, fuel="diesel"):
        super().__init__(make, model, fuel)

class Motorcycle(Vehicle):
    number_of_wheels = 2

 
my_truck = Truck("Ford", "F350")
print(f"my_truck is type {type(my_truck)}")
print(f"my_truck uses {my_truck.fuel}")
print(f"my_truck has {my_truck.number_of_wheels} wheels")
