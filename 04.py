"""
Declare a variable named company and assign it to an initial value "Coding For All".
Change all the characters to uppercase letters using upper() method.
Change all the characters to lowercase letters using lower() method.
Use capitalize(), title(), swapcase() methods to format the value of the string Coding For All.
Cut(slice) out the first word of Coding For All string.
Check if Coding For All string contains a word Coding using the method index, find or other methods.
Replace the word coding in the string 'Coding For All' to Python
Split the string 'Coding For All' using space as the separator (split()) .
"Facebook, Google, Microsoft, Apple, IBM, Oracle, Amazon" split the string at the comma.
"""

str_var = "Coding For All"
str_var_2 = "Facebook, Google, Microsoft, Apple, IBM, Oracle, Amazon" 

print(str_var.upper())
print(str_var.lower())
print(str_var.capitalize())
print(str_var.title())
print(str_var.swapcase())
print(str_var[0:6])
print(str_var.find('All'))
print(str_var.index('All'))
print(str_var.replace('Coding', 'Python'))
print(str_var.split())
print(str_var_2.split(','))
print(str_var[0])