# list_loops.py filename
# Chapter 4 : Looping with list
students = ['svetlana', 'elyor', 'albina', 'giorgi']

print(f"Hello {students[0].title()}, welcome to the class!")
print(f"Hello {students[1].title()}, welcome to the class!")
print(f"Hello {students[2].title()}, welcome to the class!")

print("# FOR LOOP")
# for tempvar in listname:
# some code to repeat

for student in students:
    # this is comment line
    print(f"Hello {student.title()}, welcome to the class!")
    print('Thank you')
    print('----------')

print("this is not to repeat. Yahoo!")

nums = [8, 5, 6, 7, 2]
# at the end print the list of squares
nums_squares = []  # empty list
for num in nums:
    print(f"each number : {num}")
    print(f"square of this number is: {num ** 2}")
    print(f"square of this number is: {num * num}")
    nums_squares.append(num ** 2)

print(nums_squares)
# hw: 4-1, 4-2

# Summary:
# list: create, access, add, modify, remove
# list: list.sort(), list.sort(reverse=True),
# list: newlist = sorted(list), newlistdesc = sorted(list, reverse=True)
# list: list.reverse()
# looping : for var in list: , indentation, inside for loop, outside loop


# HOMEWORKS:  *****************************

pizzas = ['pepperoni', 'extra cheese', 'sausage', 'peppers']
for pizza in pizzas:
    print(f"i like {pizza} pizza.")
print("i really love pizza!")

animals = ["cat", "dog", "ratty"]
# animal = 'snake' - dont create the same variable name with loop variable.
# print(animal)
for animal in animals:
    print(f"a {animal} would make a great pet.")
print("these animals make great house pets!")
# print(animal) - outside of the scope
# scope of animal variable = life variable


# Homework
favorite_pizzas = ["Cheese", "Vegetable", "BBQ chicken"]
for pizza in favorite_pizzas:
    print(pizza)

favorite_pizzas = ["Cheese", "Vegetable", "BBQ chicken"]
for pizza in favorite_pizzas:
    print(f"I like {pizza} pizza")
print("I really love pizza!\n")

animals = ["Rabbit", "Bird", "Fish"]
for animal in animals:
    print(animal)

animals = ["Rabbit", "Bird", "Dog"]
for animal in animals:
    print(f"A {animal.lower()} would make a great pet")
print("Any of these animals would make a great pet")

pizzas = ['pepperoni', 'four cheese', 'mushroom']
for pizza in pizzas:
    print(pizza.title())

for pizza in pizzas:
    print('\nI like ' + pizza + ' pizza')

print('\nI really love pizza!')

animals = ['bears', 'hedgehogs', 'snakes']
for animal in animals:
    print(animal.title() + ' sleep during the winter.\n')
print('You will not find any of these animals at winter')
# 4-1. Pizzas
pizzas = ['Classic', 'Vegan', 'Sausage']
print(pizzas)
for pizza in pizzas:
    print(f"I like {pizza} pizza.")
print("I like to eat pizza once in a while.")

# 4-2. Animals
animals = ['dog', 'kitten', 'parrot']
for animal in animals:
    print(f"A {animal} will make a great pet.")
print("These animals would make a great friend!")
##########
#####4-1, 4-2
pizzas = ["Pepperoni", "Hawaiian", " Margarita"]
print(pizzas)
for pizza in pizzas:
    print(f'I like {pizza.title()} pizza very much!')

####4-2
pets = ['Dog', 'Cat', 'Ferret']
print(pets)
for pet in pets:
    print(f'A' + ' ' + pet.title() + ' ' + 'would make a great pet.')
print(f'Any of these animals {pets} would make a great pet!')

##########
pizzas = ['pepperoni', 'sicilian', 'neopolitan', 'detroit']
for pizza in pizzas:
    print(f"I like {pizza.title()}, More than other!")
print("There are very tasty")
