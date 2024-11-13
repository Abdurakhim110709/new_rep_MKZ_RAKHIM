from random import randint, choice


class GameEntity:
    def __init__(self, name, health, damage):
        self.__name = name
        self.__health = health
        self.__damage = damage

    @property
    def name(self):
        return self.__name

    @property
    def health(self):
        return self.__health

    @health.setter
    def health(self, value):
        if value < 0:
            self.__health = 0
        else:
            self.__health = value

    @property
    def damage(self):
        return self.__damage

    @damage.setter
    def damage(self, value):
        self.__damage = value

    def __str__(self):
        return f'{self.__name} health: {self.health} damage: {self.damage}'


class Boss(GameEntity):
    def __init__(self, name, health, damage):
        super().__init__(name, health, damage)
        self.__defence = None

    def choose_defence(self, heroes):
        hero = choice(heroes)
        self.__defence = hero.ability

    def attack(self, heroes):
        for hero in heroes:
            if hero.health > 0:
                if type(hero) == Berserk and self.__defence != hero.ability:
                    hero.blocked_damage = choice([5, 10])
                    hero.health -= (self.damage - hero.blocked_damage)
                else:
                    hero.health -= self.damage

    @property
    def defence(self):
        return self.__defence

    def __str__(self):
        return 'BOSS ' + super().__str__() + f' defence: {self.__defence}'


class Hero(GameEntity):
    def __init__(self, name, health, damage, ability):
        super().__init__(name, health, damage)
        self.__ability = ability

    @property
    def ability(self):
        return self.__ability

    def attack(self, boss):
        boss.health -= self.damage

    def apply_super_power(self, boss, heroes):
        pass


class Witcher(Hero):
    def __init__(self, name, health, damage):
        super().__init__(name, health, damage, 'Revival')

    def apply_super_power(self, boss, heroes):
        for hero in heroes:
            if hero.health == 0:
                hero.health = self.health
                self.health = 0
                print(f'Witcher {self.name}, revived {hero.name} ')




class Warrior(Hero):
    def __init__(self, name, health, damage):
        super().__init__(name, health, damage, 'CRITICAL_DAMAGE')

    def apply_super_power(self, boss, heroes):
        crit = self.damage * randint(2, 5)
        boss.health -= crit
        print(f'Warrior {self.name} hit critically {crit} to boss.')


class Magic(Hero):
    def __init__(self, name, health, damage):
        super().__init__(name, health, damage, 'BOOST')

    def apply_super_power(self, boss, heroes):
        for hero in heroes:
            hero.damage += 10


class Deku(Hero):
    def __init__(self, name, health, damage):
        super().__init__(name, health, damage, 'CHANGE DAMAGE POWER')

    def apply_super_power(self, boss, heroes):
        rand_rate = choice([1.2, 0.5, 0.3, 0.8, 1.5])
        self.damage = int(self.damage * rand_rate)
        if rand_rate > 1:
            self.health -= self.damage
            print(f'Deku {self.name} increased damage!')
        else:
            print(f'Deku {self.name} decreased damage!')



class Hacker(Hero):
    def __init__(self, name, health, damage):
        super().__init__(name, health, damage, 'Hack')

    def apply_super_power(self, boss, heroes):
        if round_number % 2 == 0:
            boss.health -= 15
            rand_hero = choice(heroes)
            rand_hero.health += 15
            print(f'Hacker {self.name} steal boss health')




class Berserk(Hero):
    def __init__(self, name, health, damage):
        super().__init__(name, health, damage, 'BLOCK_DAMAGE_AND_REVERT')
        self.__blocked_damage = 0

    @property
    def blocked_damage(self):
        return self.__blocked_damage

    @blocked_damage.setter
    def blocked_damage(self, value):
        self.__blocked_damage = value

    def apply_super_power(self, boss, heroes):
        boss.health -= self.__blocked_damage
        print(f'Berserk {self.name} reverted {self.__blocked_damage} to boss.')


class Medic(Hero):
    def __init__(self, name, health, damage, heal_points):
        super().__init__(name, health, damage, 'HEAL')
        self.__heal_points = heal_points

    def apply_super_power(self, boss, heroes):
        for hero in heroes:
            if hero.health > 0 and self != hero:
                hero.health += self.__heal_points


round_number = 0


def show_statistics(boss, heroes):
    print(f'ROUND - {round_number} ------------')
    print(boss)
    for hero in heroes:
        print(hero)


def play_round(boss, heroes):
    global round_number
    round_number += 1
    boss.choose_defence(heroes)
    boss.attack(heroes)
    for hero in heroes:
        if hero.health > 0 and boss.health > 0 and boss.defence != hero.ability:
            hero.attack(boss)
            hero.apply_super_power(boss, heroes)
    show_statistics(boss, heroes)


def is_game_over(boss, heroes):
    if boss.health <= 0:
        print('Heroes won!!!')
        return True
    all_heroes_dead = True
    for hero in heroes:
        if hero.health > 0:
            all_heroes_dead = False
            break
    if all_heroes_dead:
        print('Boss won!!!')
        return True
    return False


def start_game():
    boss = Boss(name='Dragon', health=10000, damage=50)
    decu = Deku(name='Decu', health=3003, damage=50)
    hacker = Hacker(name='Hacker', health=3001, damage=50)
    witcher = Witcher(name='Witcher', health=3001, damage=0)
    warrior_1 = Warrior(name='Mario', health=2703, damage=10)
    warrior_2 = Warrior(name='Ben', health=2801, damage=15)
    magic = Magic(name='Merlin', health=2903, damage=10)
    berserk = Berserk(name='Guts', health=2601, damage=5)
    doc = Medic(name='Aibolit', health=2504, damage=5, heal_points=15)
    assistant = Medic(name='Kristin', health=3002, damage=5, heal_points=5)
    heroes_list = [warrior_1, doc, warrior_2, magic, berserk, assistant, witcher, hacker, decu]
    show_statistics(boss, heroes_list)
    while not is_game_over(boss, heroes_list):
        play_round(boss, heroes_list)


start_game()
