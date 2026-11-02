tuple_1 = ('rumesh', 'dilshantha', 'silva')
tuple_2 = ('kasun', 'iroshan')

tuple_conct = tuple_1 + tuple_2

print(tuple_conct)
print(len(tuple_conct))

tuple_conct = list(tuple_conct)
print(tuple_conct)

tuple_conct.append('unique')
tuple_conct.append('store')

tuple_conct = tuple(tuple_conct)
print(tuple_conct)