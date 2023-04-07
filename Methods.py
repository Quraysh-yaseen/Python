# Classes can also have class methods - methods that are shared among all instances of a certain type.
# As with variables, they can be overriden in a specific instance or subclass.

# chapter_6.py

class Car:
    runs = True
    number_of_wheels = 4

    @classmethod
    def get_number_of_wheels(cls):
        return cls.number_of_wheels

    def start(self):
        if self.runs:
            print("Car is started. Vroom vroom!")
        else:
            print("Car is broken :(")

my_car = Car()
print(f"Cars have {Car.get_number_of_wheels()} wheels.")

# Of course, we can override this in our instance:
my_car.number_of_wheels = 6

# And when we access our new instance variable:
print(f"My car has {my_car.number_of_wheels} wheels.")

# But, when we call our class method on our instance:
print(f"My car has {my_car.get_number_of_wheels()} wheels.")






# the type() function returns the type of the object you pass it, or it’s class.

print (type(42))
print (type("Hello world!"))
print (type(my_car))


# The issubclass function takes two classes, and returns True if the first class is a subclass of the second

print (issubclass(bool, int))
print (issubclass(int, object))
print (issubclass(bool, object))


# The isinstance() function takes an object and a class, and returns True if the object you pass it is an instance of the class.

print (isinstance(42, int))
print (isinstance("Hello world!", str))
print (isinstance(my_car, float))
print (isinstance(my_car, Car))



""" Classes can have an optional magic method called __init__() that gets run when you instantiate an instance of a class.
 You can use the __init__() method to do any special thing you want to happen when your instance is instantiated, including setting instance variables.
 __init__ can take arguments, too. """

class Car:
    runs = True

    def __init__(self, make, model):
        self.make = make
        self.model = model

    def start(self):
        if self.runs:
            print(f"Your {self.make} {self.model} is started. Vroom vroom!")
        else:
            print(f"Your {self.make} {self.model} is broken :(")

my_car = Car("Ford", "Thunderbird")
my_car.start()



# Classes have two other magic methods that come in handy for debugging, __str__() and __repr__().
# Both functions return a string representation of an object.
#  __str__() should return readable end-user output, and __repr__() should return the Python code necessary to rebuild the object.

import datetime
now = datetime.datetime.now()
print(str(now))
print(repr(now))



class Car:
    def __init__(self, make, model):
        self.make = make
        self.model = model

    def __str__(self):
        return f"<<Car object: {self.make} {self.model}>>"

    def __repr__(self):
        return f"Car('{self.make}', '{self.model}')"

my_car = Car("Ford", "Thunderbird")
print(f"This object is a {str(my_car)}")
print(f"To reproduce it, type: {repr(my_car)}")





