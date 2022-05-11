# Errors and Exceptions

# NameError, TypeError, ZeroDivisionError, FileNotFoundError
# TimeoutError
# print(f"five divided by 5 : {5 / 5}")
# print(f"five divided by 0 : {5 / 0}")
# print(f"five divided by 0 :{5 / 10}")
# print(f"five minus 0 : {5 - 0}")

try:
    # code to run
    print(f"five divided by 5 : {5/5}")
    print(f"five minus 0 : {5+ '0'}")
    print(f"five divided by 0 : {5/0}")
    print(f"five divided by 0 :{5/10}")
except ZeroDivisionError as err:
    print("Come on! You can not divide by Zero...")
    print(err)
except TypeError as err:
    print("Casting issue, data type mismatch")
    print(err)

# except Exception as err:
#     print("All exceptions handling ")

print("---- program completed --------")