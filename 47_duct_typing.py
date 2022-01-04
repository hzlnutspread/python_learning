# Duct typing = the class of an object is less important than the methods/attributes the class has
# class type is not checked if minimum methods/attributes are present
# "If it walks like a duck, and it quacks like a duck, then it must be a duck"

class Duck:
    def walk(self):
        print("This duck is walking")

    def talk(self):
        print("This duck is quacking")


class Chicken:

    def walk(self):
        print("This chicken is walking")

    def talk(self):
        print("This chicken is clucking")


class Person:

    def catch(self, duck):
        duck.walk()
        duck.talk()
        print("You caught the critter")


duck = Duck()
chicken = Chicken()
person = Person()

person.catch(duck)
person.catch(chicken)  # this will give the correct output since the methods under duck and chicken are identical
