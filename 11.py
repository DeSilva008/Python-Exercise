"""
Declare a function add_two_numbers. It takes two parameters and it returns a sum.
"""

# def add(a, b):
#     return (a+b)

# print(add(10, 2))

"""
Write a function called add_all_nums which takes arbitrary number of arguments and sums all the 
arguments. Check if all the list items are number types. If not do give a reasonable feedback.
"""

# def add_all_numbers(*nums):
#     total = 0
#     for num in nums:
#         if type(num) == int or type(num) == float:
#             total += num
#         else:
#             print(f'{nums} is not a number types. There for can\'t be added.')

#     return total

# print(add_all_numbers(2,4,5,6,7))

# def add_all_nums(*nums):
#     total = 0
#     for num in nums:
#         if isinstance(num, (int, float)):
#             total += num
#         else:
#             print(f'{num} is neiter int nor flaot.')

#     return total

# print(add_all_nums(10,'apple',40,10))

"""Declare a function named reverse_list. It takes an array as a parameter 
and it returns the reverse of the array (use loops)."""

# def reverse_list(list):
#     new_list =[]
#     for num in range(len(list)-1,-1,-1):
#         temp = list[num]
#         new_list.append(temp)

#     return new_list

# print(reverse_list([1,3,4,5,6]))

"""Write a function called greet which takes a default argument, name. If no argument is 
supplied it should print "Hello, Guest!", otherwise it should greet the person by name."""

# def greet(name="Guest"):
#     print(f'Hellow, {name}!')

# greet()

def show_args(**kwargs):
    for key, value in kwargs.items():
        print(key, value, end="")

show_args(name="Alice", age=30, city="New York")