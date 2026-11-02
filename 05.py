"""
Declare a list variable named it_companies and assign initial values Facebook, Google, Microsoft, 
Apple, IBM, Oracle and Amazon.

Print the list using print()

Print the number of companies in the list

Print the first, middle and last company

Print the list after modifying one of the companies

Add an IT company to it_companies

Insert an IT company in the middle of the companies list

Change one of the it_companies names to uppercase (IBM excluded!)

Join the it_companies with a string '#'

Check if a certain company exists in the it_companies list.

Sort the list using sort() method

Reverse the list in descending order using reverse() method

Slice out the first 3 companies from the list

Slice out the last 3 companies from the list

Slice out the middle IT company or companies from the list

Remove the first IT company from the list

Remove the middle IT company or companies from the list

Remove the last IT company from the list

Remove all IT companies from the list

Destroy the IT companies list

Join the following lists:
    front_end = ['HTML', 'CSS', 'JS', 'React', 'Redux']
    back_end = ['Node','Express', 'MongoDB']

After joining the lists Copy the joined list and assign it to a 
variable full_stack, then insert Python and SQL after Redux.

"""

it_companies = ['Facebook', 'Googlr', 'Microsoft', 'Aplle', 'IBM', 'Oracle', 'Amazon']

print(it_companies)

print(len(it_companies))

print(f'First: {it_companies[0]} \nMiddle: {it_companies[3]} \nlast: {it_companies[6]}')

it_companies[0] = "Facebook-Meta"
print(it_companies)

it_companies.append('WSO2')
print(it_companies)

it_companies.insert(4, 'LSEG')
print(it_companies)

it_companies[0] = it_companies[0].upper()
print(it_companies)

print('#'.join(it_companies))

print('WSO2' in it_companies)

it_companies.sort()
print(it_companies)

it_companies.reverse()
print(it_companies)

print(it_companies[:3])

print(it_companies[-3:])

print(it_companies[3:6])

it_companies.remove('WSO2')
print(it_companies)

del it_companies[4]
print(it_companies)

it_companies.pop()
print(it_companies)

it_companies.clear()
print(it_companies)

del it_companies
#print(it_companies)

front_end = ['HTML', 'CSS', 'JS', 'React', 'Redux']
back_end = ['Node','Express', 'MongoDB']

front_end.extend(back_end)
full_stack = front_end.copy()
print(full_stack)

full_stack.insert(5, 'Python')
full_stack.insert(6, 'SQL')
print(full_stack)