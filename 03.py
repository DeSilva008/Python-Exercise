"""
Find the length of 'python' and 'dragon' and make a falsy comparison statement.
Use and operator to check if 'on' is found in both 'python' and 'dragon'
I hope this course is not full of jargon. Use in operator to check if jargon is in the sentence.
There is no 'on' in both dragon and python
Find the length of the text python and convert the value to float and convert it to string
"""

print(len("python") == len("dragon"))

print("on" in "python" and "on" in "dragon")

sent = "I hope this course is not full of jargon"
print("jargon" in sent)

print('on' not in 'dragon' and 'on' in 'python')

len = len("python")
print(float(len))
print(str(len))

"""
Even numbers are divisible by 2 and the remainder is zero. 
How do you check if a number is even or not using python?
"""

def check_even():
    num = int(input("Enter a number:"))
    rem = num%2
    print("Is input number is even?", rem is 0)

#check_even()

"""
Check if the floor division of 7 by 3 is equal to the int converted value of 2.7.
"""

print(7//3 is int(2.7))

