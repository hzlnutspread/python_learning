# super() = function used to give access to the methods of a parent class
# returns a temporary object of a parent class when used

class Rectangle:  # parent class
    pass


class Square(Rectangle):  # child class

    def __init__(self, length, width):
        self.length = length  # repeated in cube
        self.width = width  # repeated in cube


class Cube(Rectangle):  # child class

    def __init__(self, length, width, height):
        self.length = length  # repeated in square
        self.width = width  # repeated in square
        self.height = height


square = Square(3, 3)
cube = Cube(3, 3, 3)


# self.length and self.width are repeated. We want to reuse this code by putting it in the Rectangle class instead
# Instead we do this:

class Rectangle:  # parent class

    def __init__(self, length, width):
        self.length = length  # repeated in cube
        self.width = width  # repeated in cube


class Square(Rectangle):  # child class

    def __init__(self, length, width):
        super().__init__(length, width)  # use super().__init__ to gain access to the __init__ methods

    def area(self):
        return self.length * self.width


class Cube(Rectangle):  # child class

    def __init__(self, length, width, height):
        super().__init__(length, width)
        self.height = height

    def volume(self):
        return self.length * self.width * self.height


square = Square(3, 3)
cube = Cube(3, 3, 3)

print(square.area())
print(cube.volume())
