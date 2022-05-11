# list_loops.py filename
# Chapter 4 : Looping with list, Making Numerical Lists
# range(start, end, step)
# default start is 0, don't include End, default step is 1
print(range(5))
nums = list(range(5))
print(nums)

for num in range(2, 10, 3):
    print(num)

# problem: print squares of all even numbers from 100-150
num_list = []
for i in range(100, 150, 2):
    num_list.append(i ** 2)
print(num_list)

# statistical functions:
print("highest number:", max(num_list))
print("lowest number:", min(num_list))
print("sum of the numbers:", sum(num_list))

# List Comprehensions:
num_list1 = [(i ** 2) for i in range(2, 21, 2)]
print(num_list1)

# practice: 4-3 to 4-9
print("#### SLICING THE LIST ##############")
new_list = num_list1[1:5]
print(new_list)

# NOTE: if you don't mention start default is 0
# NOTE: if you don't mention end it means till the last element
print(num_list1[1:5])  # 1:5 means from index 1 up to index 5, not including index5
print(num_list1[:5])
print(num_list1[2:])
print(num_list1[:])

print("# Copying the list")
num_list2 = num_list1
num_list3 = num_list1[:]

print(num_list1)
print(num_list2)
print(num_list3)
num_list2.append(500)
num_list3.append(600)
print("after modifying ------------")
print(num_list1)
print(num_list2)
print(num_list3)

print("Looping through the slice of the list: ")
for num in num_list1[1:5]:
    print(num)

# practice: h/w: 4-10, 4-11, 4-12
print("# print multiplication table")
for i in range(1, 11):
    # print(i)
    for j in range(1, 11):
        print(f"{i} and {j}:j*i = {j * i}")
