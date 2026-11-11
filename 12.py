# def sum_numbers(nums):  # normal function
#     return sum(nums)    # a sad function abusing the built-in sum function :<

# def higher_order_function(f, lst):  # function as a parameter
#     summation = f(lst)
#     return summation

# result = higher_order_function(sum_numbers, [1, 2, 3, 4, 5])
# print(result)

# #===================================================================================

# def square(x):          # a square function
#     return x ** 2

# def cube(x):            # a cube function
#     return x ** 3

# def absolute(x):        # an absolute value function
#     if x >= 0:
#         return x
#     else:
#         return -(x)

# def higher_order_function(type): # a higher order function returning a function
#     if type == 'square':
#         return square
#     elif type == 'cube':
#         return cube
#     elif type == 'absolute':
#         return absolute

# result = higher_order_function('square')
# print(result(3))       # 9
# result = higher_order_function('cube')
# print(result(3))       # 27
# result = higher_order_function('absolute')
# print(result(-3))  

#================= Decorator function =====================

# # Normal function
# def greeting():
#     return 'Welcome to Python'

# def uppercase_decorator(function):
#     def wrapper():
#         func = function()
#         make_uppercase = func.upper()
#         return make_uppercase
#     return wrapper

# # g = uppercase_decorator(greeting)
# # print(g())          # WELCOME TO PYTHON

# print(uppercase_decorator(greeting)())


# Let us implement the example above with a decorator

'''This decorator function is a higher order function
that takes a function as a parameter'''

def uppercase_decorator(function):
    def wrapper():
        func = function()
        make_uppercase = func.upper()
        return make_uppercase
    return wrapper

@uppercase_decorator
def greeting():
    return 'Welcome to Python'

print(greeting())   # WELCOME TO PYTHON


# print((lambda a,b : a+b)(2,3))


# def decorator_with_parameters(function):
#     def wrapper_accepting_parameters(para1, para2, para3):
#         function(para1, para2, para3)
#         print("I live in {}".format(para3))
#     return wrapper_accepting_parameters

# @decorator_with_parameters
# def print_full_name(first_name, last_name, country):
#     print("I am {} {}. I love to teach.".format(
#         first_name, last_name))

# print_full_name("Asabeneh", "Yetayeh",'Finland')