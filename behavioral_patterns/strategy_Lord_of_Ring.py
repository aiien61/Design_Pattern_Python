from abc import ABC, abstractmethod

class WeaponBehavior(ABC):
    @abstractmethod
    def use_weapon(self): raise NotImplementedError

class KnifeBehavior(WeaponBehavior):
    def use_weapon(self):
        print('Attack with a knife.')


class AxeBehavior(WeaponBehavior):
    def use_weapon(self):
        print('Attack with an axe.')


class SwordBehavior(WeaponBehavior):
    def use_weapon(self):
        print('Attack with a sword.')


class BowAndArrowBehavior(WeaponBehavior):
    def use_weapon(self):
        print('Attack with arrows.')

class Character(ABC):
    _weapon: WeaponBehavior = None

    @property
    def weapon(self):
        return self._weapon
    
    @weapon.setter
    def weapon(self, weapon: WeaponBehavior):
        self._weapon = weapon

    @abstractmethod
    def show_identity(self): raise NotImplementedError

    def fight(self) -> None:
        self.weapon.use_weapon() 


class King(Character):
    def __init__(self):
        self.weapon = KnifeBehavior()

    def show_identity(self):
        print('I am the king.')

class Queen(Character):
    def __init__(self):
        self.weapon = BowAndArrowBehavior()

    def show_identity(self):
        print('I am the queen.')

class Knight(Character):
    def __init__(self):
        self.weapon = SwordBehavior()

    def show_identity(self):
        print('I am a knight.')

class Troll(Character):
    def __init__(self):
        self.weapon = AxeBehavior()

    def show_identity(self):
        print('I am a troll.')


def battle():
    king = King()
    king.show_identity()
    king.fight()

    queen = Queen()
    queen.show_identity()
    queen.fight()

    knight = Knight()
    knight.show_identity()
    knight.fight()

    troll = Troll()
    troll.show_identity()
    troll.fight()

if __name__ == '__main__':
    battle()