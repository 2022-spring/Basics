# Chapter 6: Looping through dictionary elements
# looping : dict(by default will be keys), dict.keys(), dict.values(), dict.items()
student = {'name': ['james bond', 'agent 007'],
           'age': 23,
           'address': '456 addre st',
           'city': 'london',
           'country': 'uk',
           'tell': '89797897'}


def looping_through_keys():
    print(" #### looping through Keys (default): ")
    for key in student:
        print(key)
        print(f"the value of this key is : {student[key]}")


def looping_with_keys():
    print("----- doing the same thing with keys() method:")
    # for key in sorted(student.keys()):
    for key in student.keys():
        print(key)
        print(f"the value of this key is : {student[key]}")


def looping_through_values():
    print(" #### looping through Values: ")
    for value in student.values():
        print(value)
        # print(f"key of the this value: {student[value]}")


def looping_through_items():
    print(" #### looping through Keys and Values with items(): ")
    for key, value in student.items():
        # print(key)
        # print(value)
        print(f"key is '{key}' and value is '{value}'")


# hw: 6-1, 6-2, 6-3
# hw: 6-4, 6-5, 6-6

# Building condition with key(), values()
# if 'age' in student:   # by default it checks within keys list
def condition_with_dictionary():
    if 'age' in student.keys():
        print("we have age key in student dictionary")


# Execution lines
condition_with_dictionary()
# looping_through_values()
# looping_with_keys()
# looping_through_keys()
# looping_through_items()
