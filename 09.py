"""
Get user input using input(“Enter your age: ”). If user is 18 or older, give feedback: You are old enough to drive. If below 18 give feedback to wait for the missing amount of years. Output:

Enter your age: 30
You are old enough to learn to drive.

Output:
Enter your age: 15
You need 3 more years to learn to drive.
"""

# user_input = int(input("Enter your age:"))

# if user_input >= 18:
#     print("you are old enough to learn to drive.")
# else:
#     print(f"You need {18 - user_input} more years to learn to drive.")


"""
Compare the values of my_age and your_age using if … else. Who is older (me or you)? Use input(“Enter your age: ”) to get the age as input. You can use a nested condition to print 'year' for 1 year difference in age, 'years' for bigger differences, and a custom text if my_age = your_age. Output:

Enter your age: 30
You are 5 years older than me.
"""

# my_age = 26
# user_age = int(input("Enter your age:"))

# if user_age > my_age:
#     print("You are year older than me.") if (user_age - my_age == 1) else print(f"You are {user_age-my_age} years older than me.")   
# elif user_age < my_age:
#     print("You are year younger than me.") if (my_age - user_age == 1) else print(f"You are {my_age - user_age} years younger than me.")       
# else:
#     print("We are same age.")


"""
Get the month from user input then check if the season is Autumn, Winter, Spring or Summer. If the user 
input is: September, October or November, the season is Autumn. December, January or February, the 
season is Winter. March, April or May, the season is Spring June, July or August, the season is Summer
"""    

# user_input = str(input("Enter the month: ")).strip().lower()

# autumn = ['September', 'October', 'November']
# winter = ['December', 'January', 'February']
# spring = ['March', 'April', 'May']
# summer = ['June', 'July', 'August']

# if user_input in list(map(str.lower, autumn)):
#     print("Season is Autumn.")
# elif user_input in list(map(str.lower, winter)):
#     print("Season is Winter.")
# elif user_input in list(map(str.lower, spring)):
#     print("Season is Spring.")
# elif user_input in list(map(str.lower, summer)):
#     print("Season is Summer.")
# else:
#     print("Wrong input. Try again.")

"""
 * Check if the person dictionary has skills key, if so print out the middle skill in the skills list.
 * Check if the person dictionary has skills key, if so check if the person has 'Python' skill and print out the result.
 * If a person skills has only JavaScript and React, print('He is a front end developer'), if the person skills has 
 Node, Python, MongoDB, print('He is a backend developer'), if the person skills has React, Node and MongoDB, 
 Print('He is a fullstack developer'), else print('unknown title') - for more accurate results more conditions can be nested!
 * If the person is married and if he lives in Finland, print the information in the following format:
    Asabeneh Yetayeh lives in Finland. He is married.
"""

person={
    'first_name': 'Asabeneh',
    'last_name': 'Yetayeh',
    'age': 250,
    'country': 'Finland',
    'is_married': True,
    'skills': ['JavaScript', 'React', 'Node', 'MongoDB', 'Python'],
    'address': {
        'street': 'Space street',
        'zipcode': '02210'
    }
    }

keys = person.keys()
skill_length = int(len(person['skills']))

if 'skills' in keys:
    if skill_length%2 == 0:
        middle = int((skill_length/2) - 1)
        print(f'Middle skills are {person['skills'][middle:middle+2]}')
    else:
        middle = int((skill_length - 1)/2)
        print(f'Middle skill is {person['skills'][middle]}')
else:
    print("There is no skill key in person")


if 'skills' in keys:
    if 'Python' in person['skills']:
        print("Yes, python is a skill.")
    else:
        print("Python is not in skills.")
else:
    print("There is no skills key.")


if 'skills' in keys:
    if 'JavaScript' and 'React' in person['skills']:
        print("Front end developer.")
    else:
        print("ERROR 404")


if person['is_married'] == True and person['country'] =='Finland':
    print(f'{person['first_name']} {person['last_name']} lives in {person['country']}. He is married.')
else:
    print("error")