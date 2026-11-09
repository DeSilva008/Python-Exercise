"""
Iterate 0 to 10 using for loop, do the same using while loop.
"""

# for num in range(11):
#     print(num)

# num = 0
# while num < 11:
#     print(num)
#     num += 1

"""
Iterate 10 to 0 using for loop, do the same using while loop.
"""

# for num in range(10,-1,-1):
#     print(num)

# num = 10
# while num >= 0:
#     print(num)
#     num += -1

"""
Write a loop that makes seven calls to print(), so we get on the output the following triangle:

  #
  ##
  ###
  ####
  #####
  ######
  #######
"""

# count = 1
# while count <= 7:
#     print(count*'#')
#     count += 1

# for num in range(1,8):
#     print(num*'#')

"""
Use nested loops to create the following:

# # # # # # # #
# # # # # # # #
# # # # # # # #
# # # # # # # #
# # # # # # # #
# # # # # # # #
# # # # # # # #
# # # # # # # #
"""

# for count in range(1,9):
#     for count in range(1,9):
#         print("#", end=" ")
#     print("")

"""
Print the following pattern:

0 x 0 = 0
1 x 1 = 1
2 x 2 = 4
3 x 3 = 9
4 x 4 = 16
5 x 5 = 25
6 x 6 = 36
7 x 7 = 49
8 x 8 = 64
9 x 9 = 81
10 x 10 = 100
"""

# for num in range(11):
#     print(f"{num} x {num} = {num*num}")

"""
Iterate through the list, ['Python', 'Numpy','Pandas','Django', 'Flask'] using a for loop and print out the items.
"""

# sample_list = ['Python', 'Numpy','Pandas','Django', 'Flask']

# for item in sample_list:
#     print(item)

"""
Use for loop to iterate from 0 to 100 and print only even numbers
Use for loop to iterate from 0 to 100 and print only odd numbers
"""

# for num in range(101):
#     if num%2 == 0:
#         print(num)

# for num in range(101):
#     if not num%2 == 0:
#         print(num)        

"""
Use for loop to iterate from 0 to 100 and print the sum of all numbers.
The sum of all numbers is 5050.
"""

# total = 0
# for num in range(101):
#     total += num

# print(f'The sum of all numbers is {total}')

"""
Use for loop to iterate from 0 to 100 and print the sum of all evens and the sum of all odds.

The sum of all evens is 2550. And the sum of all odds is 2500.
"""

# odd_total = 0
# even_total = 0

# for num in range(101):
#     if num%2 == 0:
#         even_total += num
#     else:
#         odd_total += num

# print(f'the sum of all even is {even_total}. and the sum of all ods is {odd_total}')

"""
Go to the data folder and use the countries.py file. Loop through the countries and 
extract all the countries containing the word land.
"""

# import countries

# land_countries = []
# for country in countries.countries:
#     if 'land' in country.lower():
#         land_countries.append(country)

# print('Countries containing word \"land\": ', end="")
# for c in land_countries:
#     print(c, end=", ")

"""
This is a fruit list, ['banana', 'orange', 'mango', 'lemon'] reverse the order using loop
"""

# fruits = ['banana', 'orange', 'mango', 'lemon']
# revrs_fruit = []
# for x in range(len(fruits)-1,-1,-1):
#     revrs_fruit.append(fruits[x])

# print(revrs_fruit)

"""
Go to the data folder and use the countries_data.py file.
What are the total number of languages in the data
"""

from countries_data import details

print(len(details))

languages = []
for x in range(len(details)):
    languages.extend(details[x]['languages'])

print(len(languages))
languages.sort()
print(languages)

distinct_languages = set(map(lambda word: word.strip().lower(), languages))

print(len(distinct_languages))
print(distinct_languages)

"""
Find the ten most spoken languages from the data
"""

distinct_languages_list = list(distinct_languages)
distinct_languages_list.sort()

languages = [ word.strip().lower() for word in languages]
print(languages)

print(distinct_languages_list)

count = {}
for x in range(len(distinct_languages_list)):
    count[distinct_languages_list[x]] = languages.count(distinct_languages_list[x])
    print(f'{distinct_languages_list[x]} count = {languages.count(distinct_languages_list[x])}')

print(count)

top_10 = sorted(count.items(), key=lambda x: x[1], reverse=True)[:10]

print(top_10)

sorted