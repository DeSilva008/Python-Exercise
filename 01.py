"""
Exercise-01

01. Open the python interactive shell and do the following operations. The operands are 3 and 4.
    addition(+)
    subtraction(-)
    multiplication(*)
    modulus(%)
    division(/)
    exponential(**)
    floor division operator(//)
02. Write strings on the python interactive shell. The strings are the following:
    Your name
    Your family name
    Your country
    I am enjoying 30 days of python
03.Check the data types of the following data:
    10
    9.8
    3.14
    4 - 4j
    ['Asabeneh', 'Python', 'Finland']
    Your name
    Your family name
    Your country

a). Create a folder named day_1 inside 30DaysOfPython folder. Inside day_1 folder, 
create a python file helloworld.py and repeat questions 1, 2, 3 and 4. Remember to 
use print() when you are working on a python file. Navigate to the directory 
where you have saved your file, and run it.

b). Write an example for different Python data types such as Number(Integer, 
Float, Complex), String, Boolean, List, Tuple, Set and Dictionary.

c). Find an Euclidean distance between (2, 3) and (10, 8)

"""


#a)
print("3 + 4=", 3+4 , ", 3 - 4= ", 3-4, ", 3 * 4=", 3*4, ", 3 % 4=",
       3%4, ", 3 / 4=", 3/4, ", 3 ** 4= ", 3**4, ", 3 // 4=", 3//4)

var = ['asabeneh', 'Python']
your_name = "Rumesh"

print(type(10))
print(type(3.14))
print(type(4 - 4j))
print(type(your_name))
print(type(var))

def Eculidean_distance():
    x_1, y_1, x_2, y_2 = 2, 3, 10, 8

    dis = ((x_1 - x_2)**2 + (y_1 - y_2)**2)
    print("Euclidean distance is:", dis)

Eculidean_distance()