# multiple inheritance = when a child class is derived from more than one parent class

class Prey:

    def flee(self):
        print("This animal flees")


class Predator:

    def hunt(self):
        print("This animal is hunting")


# we want to create an animal that can do either or both of these parent classes
class Rabbit(Prey):
    pass


class Hawk(Predator):
    pass


class Fish(Prey, Predator):
    pass


rabbit = Rabbit()
hawk = Hawk()
fish = Fish()
