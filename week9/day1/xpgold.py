class Character:
    def __init__(self, power, lifepoints):
        self.power = power
        self.lifepoints = lifepoints
        self.creation()


class Warrior(Character):
    def attack(self, other):
        other.lifepoints -= 10

    def creation(self):
        print('Grrrr')


class Sorcerer(Character):
    def sorcer(self, other):
        other.power += 10

    def creation(self):
        print('wooba lubba dub dub')


class Drood(Character):
    def heal(self, other):
        other.lifepoints += 10

    def creation(self):
        print('Hello World!')

my_warrior = Warrior(100, 80)
my_drood = Drood(100, 100)
# my_drood.heal(my_warrior)
# print(my_warrior.lifepoints)
