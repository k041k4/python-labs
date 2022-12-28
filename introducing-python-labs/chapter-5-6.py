# print
#print("newline\nnew\ttab")
#print("inline\"onee\\ides")
#print('Na' * 3)

# slice
letters = 'abcdefghijklmnopqrstuvwxyz'
print(letters[10:])
print(letters[10:20:2])
print(letters[::2])
print(letters[-3:])
print(letters[::-1])

# len
print(len("whatever"))

# split & join
cities = 'blava,LA,NY,Komarno'
cities_list = cities.split(',')
cities_string = '-'.join(cities_list)
print(cities_list,'\n'+cities_string)

# replace
cities = 'blava,LA,NY,Komarno'
print(cities.replace('LA', 'Washington'))

# strip
world = "!!     world  "
print(world.strip())
print(world.lstrip())
print(world.strip('!'))
print(world.upper().strip('!').strip())

# formating
thing = 'dog'
place = 'lake'
print('The {0} is in the {1}'.format(thing, place))
print('The {thing_here} is in the {place_here}'.format(thing_here=thing, place_here=place))

taxonomy = {'thing':'duck', 'place':'lake'}
print('The {0[thing]} is in the {0[place]}'.format(taxonomy))
print(f'The {thing} is in the {place}')
print(f'{thing =}, {place =}')

#print(f'The {taxonomy[0].thing} is in the {taxonomy[0].place}')

# for
for letter in cities:
    if letter == 'Y':
        break
    elif letter == ',':
        continue
    print(letter)

for x in range(0,3):
    print(x)

print(list(range(0,3)))