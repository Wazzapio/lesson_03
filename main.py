# alice = "Alice"
# b = "Bob"
# def print_names(name1, name2 = "Bob"):
#     print(f'Hello, {name1}! Hello, {name2}!')
#     # return None
#
# print_names(alice, b)


# def print_many_names(**kwargs):
#     for name in kwargs.keys():
#         print(f'Hello, {name, kwargs[name]}!')
#     # return None
#
# print_many_names(g1 = 'Bill', g2 = 'Basil', g3 = 'Bob')

# def print_None(a = None):
#     print(a)
# def user_info(name, mobile, email = None, phone = None):
#     print(f'User info; {name}, {mobile}, {email}, {phone}')
# user_info('Basil', '000')

# def random_func(x, y):
#     global z
#     z = x + y
#     return chr(z)
# print(random_func(25, 36))
# print(z)

"""

lambda x: x**2
"""

features = [{'название': 'computer', 'цена': '500', 'количество': '3'},
            {'название': 'tv', 'цена': '200', 'количество': '5'},
            {'название': 'printer', 'цена': '300', 'количество': '1'}]

features_sorted_price = sorted(features, key = lambda x: int(x['цена']*80))
print(features_sorted_price)
