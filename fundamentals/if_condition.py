# Chapter 5 : IF statements

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

# if condition:
#     code block, when condition is true
# else:
#     code block, when condition is false

if num > 4:  # required, starting statement
    print("Num is greater than 4 ...")
    print("do something if greater than 4")
elif num == 4:  # optional but non-starting statement
    print("Num is equal to 4")
else:  # optional statement
    print("Num is less than 4")

# (bal <= transfer )

cars = ['audi', 'bmw', 'subaru', 'toyota']
for car in cars:
    if car == 'bmw':
        print("if we see bmw >>>", car.upper())
    else:
        print("all other cars >>>", car.title())

# problem solving:
print("---------- Program starting .... ------------------")
# yes or no if the phrase has vowels (a,e,i,u,o)
# msg = input("Enter your phrase here:")  # result of input is always string
msg = "ab"  # result of input is always string
print("you entered:", msg)

# phseudo code
# create vowels phrase(list)
# loop the msg for each character
# check if each character is in the vowels (list)
# when we see the vowels print "You have vowels in the phrase"
# then stop the process
# print that "Program is completed!"

vowels = 'aeiou'
for letter in msg:
    if letter in vowels:
        print("You have vowels in the phrase")
        break  # no more looping if code reach this line
    else:
        print("Vowels can not be seen so far, still looking ....")
print("Program is completed!")

# hw: print the number of vowels in the phrase
age = 30
age = age + 2  # this means incrementing the age by 2
age += 2  # the same thing as above
age = age - 2  # decrementing the age by 2
age -= 2

# hw: print the number of vowels in the phrase
msg = input("enter your phrase here:")
print("you entered:", msg)
vowels = 'aeiou'
vowel_count = 0
for letter in msg:
    if letter.lower() in vowels:
        print("you have vowels in the phrase")
        vowel_count += 1
    else:
        pass
        # print("vowels can not be seen so far, still looking ...")
print(f"you have {vowel_count} vowels in your phrase")
print("program is completed")

# Bug: if user enters upper case letter it is not defining the vowels
# fix: add capital letters in to the vowels list
# fix: line 75. letter.lower()

# Swapping the values
a = 456
b = 789
print(a, b)
# c = a
# a = b
# b = c

# a, b = b, a  # python way of swapping
print(a, b)

favs = '678'
for my_numb in msg:
    if my_numb in favs:
        print("You have my_numbs in the line")
        break
    else:
        print("my_numbs can not so far ")
print("completed")
# ------
vowels = "aeiou"
not_found = 0  # not vowels
found = 0  # vowels

msg = input("Please enter you phrase: \n")

for letter in msg:
    if letter in vowels:
        found += 1
        print(f" I have found a vowel in your phrase {found} time. ")
    else:
        not_found += 1
        print(f"Did not find  : {not_found} time. ")

print(f"This loop went through {msg.upper()}  and found vowels : {found} times!!! \n"
      f"and did not found vowels in {msg.upper()} : {not_found} times!!!! \n"
      f"Total times : {found + not_found}")

## 4-6

for num in range(1, 21):
    if num % 2 != 0:
        print(f"Odd number:{num}")
        if num % 11 == 0:
            print("this number is dividable by 11 ")

odd_num = list(range(1, 21, 2))

# 4-10 Slices
car_list = ['Honda', 'Toyota', 'Mazda', 'Chevrolet', 'Kia', 'Ford']
print("The first three items in this list are:", car_list[0:3])
print("Three items from the middle of the list are:", car_list[1:4])
print("The last three items in this list are:", car_list[3:6])
# 101, 99, 48+49+50+51 >> int(n/2)+1

# hw: print if the phrase is palindrome
# input: kayak ; output: True/it is a palindrome
# input: hello ; output: False/it is not a palindrome
