# Lists in Python  Chapter 3
# Data structure - structures that holds complex data for various purposes in a different way, depending on DS type
# Array - Mutable List : list of elements, elements can be strings, int, floats, boolean, list, dictionary or any other DS
# Tuples - Immutable list: can not be updated or added elements
# Hashing/HashMap/Map - Dictionary  -  we will go over later, dont ask me this.

message = "hello world!"
friend = "john"
number = 23  # IndentationError: unexpected indent, you need delete empty spaces in the beginning of the line

# Naming: lower case, in plural,
# list_name = [elem1, elem2, elem3 ..... ] , list elements are comma separated
#   Index >>>  0,     1,        2, ....
# list_name = []  ; list_name = list()     - this is how you create empty list
mix_list = []
mix_list = list()
mix_list = [message, 'bye bye', 'hi', 456, True, 789.999]  # you can store different data types in one list
messages = [message, "hello class", 'bye bye', 'hi']
friends = ['john', 'obama', 'trump', 'svetlana']
numbers = [23, 45, 67, 8, 11, 90]
shopping_list = (23, 34, 45)  # tuples: immutable

# print(messages, friends, numbers, sep='\n')
print(messages)
print(friends)
print(numbers)

# Access, add element, remove element.
print("This is the first value of the messages", messages[0])
print(f"This is the first value of the messages: {messages[0]}")
print(messages[1])
print(messages[2])
print(messages[3])
print(messages[-1])
print(messages[-2])
print(messages[-4])
# print(messages[4]) # IndexError: list index out of range
# H/W : 3-1, 3-2, 3-3

# Updating the values
print(friends)
friends[2] = 'mark'  # assigning new value to the specific element
print('after updating the list', friends)
# shopping_list[1] = 45  can not update elements in tuple

# Adding elements : add to the end of the list (append), insert using index in the list
# friends = ['john', 'obama', 'trump', 'svetlana']
print("Original friends list: ", friends)
friends.append('George')
print('Appended New friend a list: ', friends)
# shopping_list.append()  not possible for tuple, because it is immutable

friends.insert(1, 'Igor')
print('Inserted New friend a list: ', friends)
print("what is the index of the element? ", friends.index('svetlana'))
print("what is the value of the index? ", friends[4])

# Slicing the list
print(friends[1:3])  # this gives elements on the index 1, 2 not including index 3

# Chapter 3: page 42 : Removing an Item Using the del statement
print("# Chapter 3: page 42 : Removing an Item Using the del statement ------")

cars = ['toyota', 'nissan', 'tesla', 'honda']
print(cars)
del cars[2]
print(cars)

# using pop() - it removes the element with index and returns the same value as a result, default index is -1
deleted_car = cars.pop(1)
print(cars)
print(deleted_car)
# result = print(deleted_car) - this is not possible because print() function does not return anything
# functions (arg1, arg2 ....) >> do something Return value/list/,

# Removing the Item by value
print("# Removing the Item by value")
cars.insert(0, 'mazda')
cars.append('mercedes')
cars.append('kia')
cars.append('honda')
print(cars)
cars.remove('honda')  # removing the element by value, removes only first occurrence in the list
print(cars)

# HW: 3-4, 3-5, 3-6, 3-7

print("# Sorting a list Permanently with sort() Method")
# cars.sort()   # sorting by default in ASC order
# cars.sort(reverse=True)   # sorting in Desc order
# print(cars)

print(" # Sorting a list Temporarily with sorted() Function ")
cars_sorted = sorted(cars)  # sorted(cars, reverse=False)
cars_sorted_desc = sorted(cars, reverse=True)
print("cars_sorted: ", cars_sorted)
print("cars_sorted_desc: ", cars_sorted_desc)
print("original cars: ", cars)

# Reversing the list permanently, No sorting happens with list.reverse()
cars.reverse()
print("reversed list : ", cars)

# Finding the Length of a List - how many elements we have in the list?
num_of_cars = len(cars)
print("the length of the cars list:", len(cars))
print("the length of the cars list, with variable:", num_of_cars)
# last index is always 1 less from length of the list
print("the last index in cars list is: ", len(cars) - 1)
# print(cars[5])  # IndexError: list index out of range
# Always make sure that index provides is within range (0, len(list)-1 )
