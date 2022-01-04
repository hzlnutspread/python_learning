# An abstract class prevents a user from creating an object of that class (Just a template, a ghost class)
# It compels a user to override abstract methods in a child class

# abstract class = class which contains one or more abstract methods
# abstract method = method that has a declaration but does not have an implementation


class Vehicle:

    def go(self):
        pass


class Car(Vehicle):

    def go(self):  # the go(self) function is being overridden and adding our own implementation
        print("You drive the car")


class Motorcycle(Vehicle):

    def go(self):  # the go(self) function is being overridden and adding our own implementation
        print("You ride the motorcycle")


vehicle = Vehicle()
car = Car()
motorcycle = Motorcycle()

vehicle.go()  # this will do nothing it has not been implemented but has been declared
car.go()
motorcycle.go()

# For example, we want a user to create an object that is not of vehicle class since its too generic
# So we turn the vehicle class into an abstract class
# We do the following


from abc import ABC, abstractmethod


class Vehicle(ABC):

    @abstractmethod  # this is done before every method. Prevents us from creating this object
    def go(self):
        pass

    @abstractmethod
    def stop(self):
        pass


class Car(Vehicle):

    def go(self):  # the go(self) function is being overridden and adding our own implementation
        print("You drive the car")

    def stop(self):
        print("You stop the car")


class Motorcycle(Vehicle):

    def go(self):  # the go(self) function is being overridden and adding our own implementation
        print("You ride the motorcycle")
    # children classes should not be missing an implementations of any methods they inherit

    def stop(self):
        print("You stop the motorcycle")


vehicle = Vehicle()  # TypeError: can't instantiate abstract class Vehicle with abstract method go.
car = Car()
motorcycle = Motorcycle()

# the children classes will inherit the abstract method. This means they NEED to override the abstract method
