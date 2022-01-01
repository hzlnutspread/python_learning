class Car:
    wheels = 4  # class variable declared within class. All Car objects will have 4 wheels by default

    def __init__(self, make, model, year, colour):  # instance variables declared inside constructor (init)
        self.make = make  # instance variables
        self.model = model  # instance variables
        self.year = year  # instance variables
        self.colour = colour  # instance variables


car_1 = Car("Chevy", "Corvette", 2021, "Blue")
car_2 = Car("Ford", "Mustang", 2022, "red")

Car.wheels = 2  # this changes the class variable globally
car_1.wheels = 2  # this changes the class variable for this object

print(car_1.wheels)
print(car_2.wheels)
