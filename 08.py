"""
Create an empty dictionary called dog
Add name, color, breed, legs, age to the dog dictionary
Create a student dictionary and add first_name, last_name, gender, age, marital status, skills, country, city and address as keys for the dictionary
Get the length of the student dictionary
Get the value of skills and check the data type, it should be a list
Modify the skills values by adding one or two skills
Get the dictionary keys as a list
Get the dictionary values as a list
Change the dictionary to a list of tuples using items() method
Delete one of the items in the dictionary
Delete one of the dictionaries
"""

log = {}

log['Name'] = 'Micky'
log['Breed'] = 'Wal'
log['Color'] = 'Mix'
log['Legs'] = 5
log['Age'] = 4

print(log)

student = {}

student.update({
    'first_name': 'Rumesh',
    'last_name': 'Silva',
    'gender': 'Male',
    'age': 5,
    'maritial_status': 'single',
    'skills': ['Python', 'Scorpion', 'Paambu', 'Garadi'],
    'country': 'Sri Lanla',
    'city': 'Galgamuwa',
    'adress': {
        'street': 'pahala widiya',
        'zip_code': 200012
    }
})

print(student)

print(len(student))

print(student.keys())

print(student.values())

print(student.items())

student.pop('first_name')
student.popitem()
del student['last_name']

print(student)

del student
print(student)