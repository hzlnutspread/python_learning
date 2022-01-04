# method overriding is an ability of an object oriented programming language
# Allows a subclass (child class) to provide a specific implementation of a method that is already provided by parent

class Animal:

    def eat(self):
        print("This animal is eating")


class Rabbit(Animal):
    # override the method here
    # within child class we need to define method with matching signature
    # method's name + parameters = method signature
    def eat(self):
        print("This rabbit is eating a carrot")


rabbit = Rabbit()
rabbit.eat()
