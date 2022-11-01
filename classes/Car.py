class Car:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
        self.km_reading = 400
        print('New car created')

    def get_description(self):
        long_name = str(self.year) + ' ' + self.make + ' ' + self.model
        return long_name.title()

    def read_km(self):
        print('this car has ' + str(self.km_reading) + 'km on it')

    def update_km(self, km):
        if km >= self.km_reading:
            self.km_reading = km
        else:
            print('you cant roll back on km')


class ElectricCar(Car):
    def __init__(self, make, model, year):
        super().__init__(make, model, year)
        self.battery = Battery()

    def des_battery(self):
        print('this car has ' + str(self.battery) + 'kwh battery')

    def fill_gas(self):
        print(f'this {self.make} doesnt need gas')


class Battery():
    def __init__(self, battery_size=70):
        self.battery_size = battery_size

    def describe_battery(self):
        print('this car has a ' + str(self.battery_size) + 'kwh battery')