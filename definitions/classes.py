# chapter 9 : Class
# Class - blueprint/template/coockie cutter/model of real-world object or situation
# Object - instance of the class
# instantiation - defining the object from the class with arguments
# Each class has a Name, state(Description, attributes >> variable )
#               and Behaviour(functionalities, actions >> functions)
# constructor - function that instantiates the class, automatically executed

class Dog:
    """General model for dog."""

    # state: breed, size, age, color >> make it global to a class
    # behavior: eat(), sleep(), run(), sit()

    dog_name = ''

    def __init__(self, breed, size, age, color):  # constructor
        print("hello I am a dog")
        # print(f"description: {breed}, {size}, {age}, {color}")
        self.breed = breed
        self.size = size
        self.age = age
        self.color = color

        # print(color)
        # print(self.color)

    def describe_dog(self):
        print(f"description: {self.breed}, {self.size}, {self.age}, {self.color}")
        print(f"Name of the dog is : '{self.dog_name}'")

    def eat(self, food):
        print(f"{self.dog_name} is eating {food} ")

    def sleep(self):
        print(f"{self.dog_name} is sleeping ....")


class Restaurant:
    """ exercise 9-1"""

    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type

    def describe_restaurant(self):
        print(self.restaurant_name + ' is the chain restaurant, which is ' + self.cuisine_type + ' cuisine type')

    def open_restaurant(self):
        print(self.restaurant_name + " is open for business")


class Restaurant2:
    """ exercise 9-2"""

    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type

    def describe_restaurant2(self):
        print(f"{self.restaurant_name}, it is {self.cuisine_type} style restaurant")

