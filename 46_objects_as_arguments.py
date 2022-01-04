# passing objects as arguments
# we call a function that accepts an object as an argument as well as a colour
class Car:
    colour = None


class Motorcycle:
    colour = None


# if it is within the Car class then it will be a method of the Car class. We want separate function
def change_colour(car, colour):  # the car object is being used as an argument
    car.colour = colour


car_1 = Car()
car_2 = Car()
car_3 = Car()

bike_1 = Motorcycle()

change_colour(car_1, "red")
change_colour(car_2, "white")
change_colour(car_3, "blue")
change_colour(bike_1, "black")

print(car_1.colour)
print(car_2.colour)
print(car_3.colour)
print(bike_1.colour)
