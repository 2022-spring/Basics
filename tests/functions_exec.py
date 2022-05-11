# Python modules, imports, packages
# import functions
# from definitions.functions import greet_user, greet_user_by_name
# from definitions.functions import greet_user_by_name_age_opt as g_user
from definitions.functions import *

print("Calling the functions after this line =========")
# greet_user()
# greet_user_by_name("mark")
# # greet_user_by_name()
# # TypeError: greet_user_by_name() missing 1 required positional argument: 'user_name'

# positional arguments
greet_user_by_name_age('john', 23)
# keyword arguments
greet_user_by_name_age(age=23, user_name='akmal')
greet_user_by_name_age(user_name='akmal', age=23)

# optional parameter with default value
greet_user_by_name_age_opt('jane')
greet_user_by_name_age_opt('jane', 25)
# if you imported the functions with alias name you need to use alias name not original name
# g_user('jane')
# g_user('jane', 25)

make_shirt(msg='Hello Winter!', size=15)
make_shirt(10, 'Hello Spring!')

result = make_shirt_return(20, 'Hello SUMMMEEEERR!')
print(result)
print(make_shirt_return(20, 'Hello SUMMER!'))
print(is_a_greater_than_b(34, 55))
print(is_a_greater_than_b(55, 53))

# hw: 8-12, 8-13, 8-14
