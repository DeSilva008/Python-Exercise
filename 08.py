import pprint as pprint

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