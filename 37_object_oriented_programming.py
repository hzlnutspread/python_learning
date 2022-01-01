# Creating objects
# An object is an instance of a class and has these two things assigned to them:
# an attribute = What an object is or has (e.g. height name age weight)
# a method = What an object can do

# In order to create an object, we need to create a class
# a class = blue print to describe what attributes and methods our distinct object will have
# can create class in this module or in a separate one


# capitalise the class name
class Car:

    def __init__(self, make, model, year, colour):  # constructor, creates objects for us
        self.make = make
        self.model = model
        self.year = year
        self.colour = colour

    def drive(self):
        print("This " + self.model + " is driving")

    def stop(self):
        print("This " + self.model + " is stopped")


car_1 = Car("Chevy", "Corvette", 2021, "Blue")
car_2 = Car("Ford", "Mustang", 2022, "red")

car_1.drive()
car_2.stop()
