# Word Dictionary
e2f = {'dog':'chien',
       'cat': 'chat',
       'walrus': 'morse'}

print(e2f)
print('walrus =', e2f.get('walrus'))

f2e = {}
for english, french in e2f.items():
    f2e.update({french : english})

print(f2e)
print('chien =', f2e.get('chien'))

# Life Multi-level dictionary
life = {'animals' : {'cats': ['Henri', 'Grumpy', 'Lucy'],
                     'octopi': {},
                     'emus': {}},
        'plants' : {},
        'others' : {}}

for toplife in life.keys():
    print(toplife)

print(list(life.keys()))
print(list(life['animals'].keys()))
print(life['animals']['cats'])

# Squares {key: key_value}
squares = {key: key*key for key in range(10)}
print(squares)

# Odd {numbers}
odd = {xnumber for xnumber in range(10) if xnumber % 2 == 1}
print(odd)

# generator comprehension - for in for
for thing in ('Got %s' % xnumber for xnumber in range(10)):
    print(thing)