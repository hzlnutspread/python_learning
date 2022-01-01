# Inheritance =
# classes can inherit attributes and methods from another class
# these classes form a parent/child relationship

class Animal:
    alive = True

    def eat(self):
        print("This animal is eating")

    def sleep(self):
        print("This animal is sleeping")


# Rabbit is the child class and animal is the parent class
class Rabbit(Animal):

    def run(self):
        print("This rabbit is running")


class Fish(Animal):

    def swim(self):
        print("This fish is swimming")


class Hawk(Animal):

    def fly(self):
        print("This hawk is flying")


rabbit = Rabbit()  # object 1
fish = Fish()  # object 2
hawk = Hawk()  # object 3

print(rabbit.alive)
fish.eat()
hawk.sleep()

rabbit.run()
fish.swim()
hawk.fly()
