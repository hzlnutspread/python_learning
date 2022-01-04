# method chaining = Calling multiple methods sequentially
# each call performs an action on the same object and return self

class Car:

    def turn_on(self):
        print("You start the engine")
        return self  # when calling method, if nothing is returned python will return None. We must add this line

    def drive(self):
        print("You drive the car")
        return self

    def brake(self):
        print("You step on the brakes")
        return self

    def turn_off(self):
        print("You turn off the engine")
        return self


car = Car()

# we want to have the car turn on and then drive. Instead of writing this:
car.turn_on()
car.drive()

# we do this instead. This chains the methods together:
car.turn_on().drive()
# when python finishes the car.turn_on() method, it will return self (car)
# since self (car) is returned, then the next method of car.drive() will be performed.

# So if we want to brake and then turn off the car we do the following:
car.brake().turn_off()

# for ease of reading we would turn this:
car.turn_on().drive().brake().turn_off()

# into this. (The backslashes are inserted automatically)
car.turn_on() \
    .drive() \
    .brake() \
    .turn_off()
