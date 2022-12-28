class Dog():
    count = 0 #global class variable
    def __init__(self, name, size = 1):
        self.name = name
        self.size = size
        self.__dna = 'secret'  #hidden attribute
        Dog.count += 1
    def make_a_sound(self):
        print('haf, haf')
    @property
    def tail_length(self):
        return ('small' if self.size < 2 else 'medium')
    @classmethod
    def species(cls):
        print('There are', cls.count, 'dogs here!')
    @staticmethod
    def about():
        print('It has 4 legs and eats everything')
class Daschund(Dog):
    def __init__(self, name):
        super().__init__(name, 2)
        print('I was initiated with a long body!')
    def say_mama(self):
        print('Maaamaa')

# static method
Dog.about()

# making instance from class
a_dog = Daschund('Nufy')
a_dog.age = 7
print(a_dog.name, "Daschund" if issubclass(Daschund, Dog) else "neviem")
a_dog.make_a_sound()
a_dog.say_mama()

# class property
print('I hava a', a_dog.tail_length, 'tail')
a_dog.size = 1
print('NO, you have a', a_dog.tail_length, 'tail')

# class method
Dog.species()
next_dog = Dog('Werewolf',3)
Dog.species()

