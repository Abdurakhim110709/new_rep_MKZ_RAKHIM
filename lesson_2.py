class Animal:
    def __init__(self, name, age):
        self.__name = name
        self.__age = age
        self.__was_born()

    def get_age(self):
        return self.__age

    def set_age(self, age):
        if type(age) == int and age > 0:
            self.__age = age
        else:
            raise ValueError('Wrong value for age field. It must be positive number.')

    def __was_born(self):
        print(f'Animal {self.__name} was born.')

    def get_name(self):
        return self.__name

    def set_name(self, name):
        self.__name = name

    def info(self):
        return f'NAME: {self.__name}, AGE: {self.__age}, BIRTH YEAR: {2024 - self.__age}'

    def make_voice(self):
        raise NotImplementedError('Method make_voice must be implemented.')


class Fish(Animal):
    def __init__(self, name, age):
        # super().__init__(name, age)
        super(Fish, self).__init__(name, age)

    def make_voice(self):
        pass


class Cat(Animal):
    def __init__(self, name, age):
        # super().__init__(name, age)
        super(Cat, self).__init__(name, age)

    def make_voice(self):
        print('Meow')


class Dog(Animal):
    def __init__(self, name, age, commands):
        super(Dog, self).__init__(name, age)
        self.__commands = commands

    @property
    def commands(self):
        return self.__commands

    @commands.setter
    def commands(self, value):
        self.__commands = value

    def info(self):
        return super().info() + f', COMMANDS: {self.__commands}'

    def make_voice(self):
        print('Woof')


class FightingDog(Dog):
    def __init__(self, name, age, commands, wins):
        super(FightingDog, self).__init__(name, age, commands)
        self.__wins = wins

    @property
    def wins(self):
        return self.__wins

    @wins.setter
    def wins(self, value):
        self.__wins = value

    def info(self):
        return super().info() + f', WINS: {self.__wins}'

    def make_voice(self):
        print('Rrr woof')


# some_animal = Animal('Anim', 3)
# some_animal.set_age(4)
# print(some_animal.info())
# print(some_animal.get_name())

cat = Cat('Tom', 5)
# print(cat.info())

dog = Dog('Snoopy', 3, 'Sit')
dog.commands = 'Sit, run'
# print(dog.commands)
# print(dog.info())

fighting_dog = FightingDog('Reks', 1, 'Fight', 10)
# print(fighting_dog.info())

fish = Fish('Dori', 2)

animals_list = [cat, fish, dog, fighting_dog]
for animal in animals_list:
    print(animal.info())
    animal.make_voice()
