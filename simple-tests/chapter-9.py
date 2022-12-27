animal = 'dog'

def change_and_print_global():
    global animal
    print('before', animal)
    animal = 'cat'
    print('after', animal)

change_and_print_global()
print(animal)