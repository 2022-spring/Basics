# Palindrome

msg = input("input word to check if its a palindrome: ")
# msg = "abc"
reversed_msg = ""
for letter in msg:
    reversed_msg = letter + reversed_msg
    print(reversed_msg)
# loops
#	reversed_msg = 'a' + '' = 'a'
#	reversed_msg = 'b' + 'a' = 'ba'
#	reversed_msg = 'c' + 'ba' = 'cba'

if msg == reversed_msg:
    print("this is a palindrome")
else:
    print("this is not a palindrome")

print("------- 2nd options ------------------------")
msg = input("check if your word is a palindrome: ")
if msg == msg[::-1]:
    print("yes it is a palindrome")
else:
    print("no its not a palindrome")

# a, b = b, a
# reversed_list = list[::-1]
# reversed_str = string[::-1]

##- ----------------------------------------------
students = {}
number_of_students = 0
question = input('Do you want to add a new student? Yes/No')
while question.lower() == 'yes':
    name = input("Enter student's name:")
    students['name'] = name
    student_id = input("Enter student's ID:")
    students["Student's ID"] = student_id
    print(f"Student's Name - {name.title()} \nStudent's ID - {student_id}")
    number_of_students += 1
    print(f"We have {number_of_students} student(s)")
    print(students)

    question = input('Do you want to add a new student? Yes/No')
    if question.lower() == 'no':
        print('See you next time. Thank you!')
    elif question.lower() == 'yes':
        print("Entering next student ....")
    else:
        print("invalid input, closing the program ..")

# --------------------------------------
import time

print("Hello user!!")
time.sleep(2)
print("\033[1;30;47m Let's play a small game.You will type a word and I will check if \n"
      "that word is Palindrome!!")
time.sleep(3)
print("Note- If you want to finish , press X .")

msg = ""
while msg.lower() not in ["x"]:
    msg = input(" Please enter a word:\n")
    if msg.lower() != "x":
        rev_word = msg[::-1]
        if msg.strip().isdigit():
            print("Sorry this is digits , only letters accepted!!!")
        elif msg.lower() == rev_word.lower():
            print(f"Wow , you got it ,  {msg} is a palindrome!!!\n"
                  f"Because  you can read it backwords too --- {msg.lower()} = {rev_word.lower()}.")
        else:
            print(f"Looks like {msg.lower()} it's not a palindrome!!")
    elif msg.lower() == "x":
        print("See you next time. Thanks")
        break


# -------------------
def is_palindrome(s):
    return s == s[::-1]


# - -----
msg = input("Enter string here: ")
revstr = (msg[::-1])
while msg in revstr:
    print('True: this is a palindrome')
    # break
if revstr not in msg:
    print('False: this is not palindrome')
