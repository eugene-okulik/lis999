my_dict = {
    'tuple': (27, 33, 33, 29, 36),
    'list': ['Mark', 'Woody', 'Shasha', 'Marzuq', 'Jianyu'],
    'dict': {
        'age': 25,
        'ethnicity': 'caucasian',
        'gender': 'male',
        'skin color': 'pale white',
        'hair length': 'short',
    },
    'set': {12, 25, 40, 8, 94}
}

print(my_dict['tuple'][-1])
my_dict['list'].append('Kia')
del my_dict['list'][1]
my_dict['dict']['I am a tuple'] = False
del my_dict['dict']['skin color']
my_dict['set'].add(4)
my_dict['set'].remove(94)
print(my_dict)
