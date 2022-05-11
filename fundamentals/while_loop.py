num = 4  # setting the value, defining/assigning
favs = list(range(10, 21))
keyword = 'abrakadabra'

# Expressions to generate True/false condition
print("num == 4:", num == 4)  # we are comparing the value of num to 5, returns True/false
print("num > 4:", num > 4)
print("num < 4:", num < 4)
print("num != 4:", num != 4)
print("num is in the favs?", num in favs)
print("num is in not the favs?", num not in favs)
print("letter 'e' in the keyword?", 'e' in keyword)

while num < 10:
    print(f"num is still less than 10, '{num}'")
    num += 1

print("==========================")
num1 = 4
while num1 > -2:
    print(f"num is still less than 10, '{num1}'")
    num1 -= 1

print("\t GAME IS STARTING \t  ------>>>>>")
name = ""
# while name.lower() not in ['exit', 'x', 'close']:
#     name = input("Enter your name :")
#     print(f"Hello {name.title()}!! Welcome to New Game!!")
# print("Game over!! See you next time ): ")
# ==============================
number = 0
answer = ''
while answer.lower() not in ['n']:
    number = int(input("Enter your number (only number are accepted): "))
    # number = int('34')
    if number % 2 == 0:
        print(f"you entered EVEN number: {number}")
    else:
        print(f"you entered ODD number: {number}")
    answer = input("Do you want to continue: y/n")
print("Game over!! See you next time ): ")

# bug: float, special, whitespace >> returns ValueError