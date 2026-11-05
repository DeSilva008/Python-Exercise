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

user_input = str(input("Enter the month: ")).strip().lower()

autumn = ['September', 'October', 'November']
winter = ['December', 'January', 'February']
spring = ['March', 'April', 'May']
summer = ['June', 'July', 'August']

if user_input in list(map(str.lower, autumn)):
    print("Season is Autumn.")
elif user_input in list(map(str.lower, winter)):
    print("Season is Winter.")
elif user_input in list(map(str.lower, spring)):
    print("Season is Spring.")
elif user_input in list(map(str.lower, summer)):
    print("Season is Summer.")
else:
    print("Wrong input. Try again.")