"""
01. The radius of a circle is 30 meters.
    i. Calculate the area of a circle and assign the value to a variable name of area_of_circle
    ii. Calculate the circumference of a circle and assign the value to a variable name of 
    circum_of_circle
    iii. Take radius as user input and calculate the area.

02. Use the built-in input function to get first name, last name, country and age from a user and 
store the value to their corresponding variable names

03. Run help('keywords') in Python shell or in your file to check for the Python reserved words or keywords

"""

#01

import math

def radius():
     r = 30

     area_of_circle = math.pi*r*r
     print("Area:", area_of_circle)

     circum_of_circle = math.pi*r*2
     print("Cirum:", circum_of_circle)

     radius = int(input("Input radius:"))

     area_of_circle = math.pi*radius*radius
     print("Area:", area_of_circle)

     circum_of_circle = math.pi*radius*2
     print("Cirum:", circum_of_circle)

radius()
