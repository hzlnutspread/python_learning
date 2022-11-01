import Car
import Contact_Data_Utils
import Contact_Data

my_car = Car.Car('audi', 'a4', 2021)
car_description = my_car.get_description()

print(car_description)

my_electric_car = Car.ElectricCar('mazda', 'g12', 2019)
my_electric_car.battery = 45
my_electric_car.des_battery()
my_electric_car.fill_gas()

data_to_search = Contact_Data.contacts
data_util = Contact_Data_Utils

data_util.search_user_email("steve rogers", data_to_search)
data_util.search_user_phone("steve rogers", data_to_search)

for key in data_to_search:
    print(key, '= ', data_to_search[key]['email'])