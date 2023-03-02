# You can think of a class as a “type” of something, like “Car.” You can think of an instance as a specific thing, such as “my Subaru,” which is a type of “Car.”

class Car:
    runs = True

    def start(self):
        if self.runs:
            print("Car is started. Vroom vroom!")
        else:
            print("Car is broken :(")

my_car = Car()
print(f"My car runs: {my_car.runs}")
my_car.start()

my_car2 = Car()
my_car2.runs = False
my_car2.start()




