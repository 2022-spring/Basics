# from definitions.classes import Dog, Restaurant, Restaurant2
from definitions.classes import *

# instantiation of Dog class, instance of class, dog1 is an object
# even you dont have constructor python will create an empty constructor when you create an object
# dog0 = Dog()
dog1 = Dog('german shepard', 'large', 5, 'black')
dog2 = Dog('maltese', 'small', 2, 'white')
dog3 = Dog('chow chow', 'medium', 3, 'brown')

dog1.dog_name = 'Rex'
dog2.dog_name = 'Max'
dog3.dog_name = 'Bob'

dog1.describe_dog()
dog2.describe_dog()
dog3.describe_dog()

print('color of dog1: ', dog1.color)

dog1.sleep()
dog2.sleep()
dog3.sleep()
dog1.eat('meat')
dog2.eat('bones')
dog3.eat('shoes')

# hw: 9-1, 9-2, 9-3
# next : Working with Classes and Instances (page 167)
# Albina:
print("------9-1------Restaurant")
r = Restaurant('Olive Garden', 'Italian')
print(f'argument1 : {r.restaurant_name} and argument2: {r.cuisine_type}')
r.describe_restaurant()
r.open_restaurant()

print("----9-2 Three Restaurants")
name1 = 'Olive Garden'
name2 = 'TGI Fridays'
name3 = 'Texas Roadhouse'
r1 = Restaurant2(name1, "italian")
r2 = Restaurant2(name2, 'american')
r3 = Restaurant2(name3, 'mexican')

r1.describe_restaurant2()
r2.describe_restaurant2()
r3.describe_restaurant2()
