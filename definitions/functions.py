# Chapter 8: Functions
def greet_user():
    print('Hello User!!')
    print("Welcome to Virtual Reality Game!")
    print("-----------------------------------")


def greet_user_by_name(user_name):
    print(f'Hello {user_name.title()}!!')
    print("*** Welcome to Virtual Reality Game! ***")
    print("-----------------------------------")


def greet_user_by_name_age(user_name: str, age: int):
    print(f'Hello {user_name.title()}!!')
    print(f"{user_name.title()}, next year you will be {age + 1} years old...")
    print("*** Welcome to Virtual Reality Game! ***")
    print("-----------------------------------")


def greet_user_by_names_age(user_names: list, age: int):
    for user_name in user_names:
        print(f'Hello {user_name.title()}!!')
        print(f"{user_name.title()}, next year you will be {age + 1} years old...")
    print("*** Welcome to Virtual Reality Game! ***")
    print("-----------------------------------")


def greet_user_by_name_age_opt(user_name, age=20):
    # age is now optional and default value is 20
    print(f'Hello {user_name.title()}!!')
    print(f"{user_name.title()}, next year you will be {age + 1} years old...")
    print("*** Welcome to Virtual Reality Game! ***")
    print("-----------------------------------")


# Java method:
# public static void main(String[] args) {
#     myMethod();
# }
# parameter (you define when you create a function) vs argument (you pass to the function when execute)

# Exercises: 8-3, 8-4, 8-5
def make_shirt(size, msg):
    """
    This is a function to make a shirt with given size and message to be printed on the shirt.
    :param size: it is a size of the shirt
    :param msg: message to be printed
    """
    print(f"Creating a shirt with size {size} and that says '{msg}' on it.")


# Functions with Return values:
def make_shirt_return(size, msg):
    return f"Creating a shirt with size {size} and that says '{msg}' on it."


def is_a_greater_than_b(a: int, b: int):
    return a > b

