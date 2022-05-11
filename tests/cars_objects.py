from definitions.cars import *

car1 = Car('toyota', 'camry', '2022')

car1.get_descriptive_name()
car1.read_odometer()
print("### updating the attribute, odometer_reading")
car1.__odometer_reading = 5000
# it is not doing anything, if variable is encapsulated
car1.get_descriptive_name()
# car1.odometer_reading = 2000
car1.set_odometer(2000)
car1.get_descriptive_name()

car1.make = 'moyota'

# Object Oriented Programming Concepts:
# Classes, Objects
# Encapsulation - hiding from object from other classes

# Inheritance :
print("*********** Inheritance : *********")
b1 = B('tesla', 'modelx', '2022')
b1.get_descriptive_name()
print("##############################")
tesla1 = ElectricCar('tesla', 'modelY', '2021')
tesla1.set_odometer(7000)
tesla1.get_descriptive_name()
tesla1.year = 2022
tesla1.get_descriptive_name()

# car1.battery_size = 0 not from the Car class
# battery_size exists only in child class
tesla1.battery_size = 110

# car1.describe_battery()
# describe_battery() has
tesla1.describe_battery()

batcar1 = BatmanCar('Nightmare', 'bat', 2030)
batcar1.fly()
batcar1.drive_fast()
batcar1.get_descriptive_name()

print("-------- Polymorphism: Method Overriding ----------")
car1.get_descriptive_name()
tesla1.get_descriptive_name()

print("length of string", len('hello'))
print("length of list", len([3, 4,5, 8]))
print("length of dictionary", len({'k1': 23, 'k2': 456}))

# H/W : 9-6 to 9-9
