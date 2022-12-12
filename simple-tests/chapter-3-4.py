# empty is false
#some_list = []
#if some_list:
#    print("not empty")
#else:
#    print("empty")

# search in string
#slovo = 'abcdefgh'
#if 'c' in slovo:
#    print('je tam')
#else:
#    print ('neni')

# search in list
#slovo = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']
#if 'c' in slovo:
#    print('je tam')
#else:
#    print ('neni')

# search in dictionary
slovo = {'a': 'apple',
        'b': 'beat',
        'c': 'cordoba',
        'd': 'delta',
        'e': 'eminem',
        'f': 'factor',
        'g': 'g-string',
        'h': 'health'}
if diff := 'c' in slovo:
    print(diff, 'je tam')
else:
    print (diff, 'neni')