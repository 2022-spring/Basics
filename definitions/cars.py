# Chapter 9

class Car:
    def __init__(self, make, model, year):
        """Initialize attributes to describe a car."""
        self.make = make
        self.model = model
        self.year = year
        self.__odometer_reading = 0  # encapsulated variable
        self.__logo = 'id="header-logo"'

    def get_descriptive_name(self):
        print(f"Full description of the car: \n\t{self.make} "
              f"{self.model} {self.year} with {self.__odometer_reading} miles on it.")

    def read_odometer(self):
        """Print a statement showing the car's mileage."""
        print(f"This car has {self.__odometer_reading} miles on it.")

    def set_odometer(self, miles):
        """Updates odometer reading. It should be more than current value."""
        # update if only new value is more than current value
        if miles > self.__odometer_reading:
            print(f"Updating the odometer to {miles}...")
            self.__odometer_reading = miles
        else:
            print(f"Odometer can not be set less than current value: {self.__odometer_reading}")


class B(Car):
    pass


class ElectricCar(Car):
    """Electric car (child) is inheriting everything from Car class"""

    def __init__(self, make, model, year):
        super().__init__(make, model, year)
        self.battery_size = 100
        self.__odometer_reading = 10

    def describe_battery(self):
        """Print a statement describing the battery size."""
        print("This car has a " + str(self.battery_size) + "-kWh battery.")

    def drive_fast(self):
        print("driving tooo fast ... :() ")

    def get_descriptive_name(self):
        print(f"Cool description of the car: \n\t{self.make} "
              f"{self.model} {self.year} with {self.__odometer_reading} miles on it.")
        print(f"Battery size is: {self.battery_size}")


class Airplane():
    def fly(self):
        print("flying ....")


class BatmanCar(ElectricCar, Airplane):
    pass

