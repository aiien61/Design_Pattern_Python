from enum import Enum
from abc import ABC, abstractmethod
from typing import List, Dict, Tuple
import random

class Role(Enum):
    SWORDSMAN = "Swordsman"
    ARCHER = "Archer"
    MAGE = "Mage"

class AttackStrategy(ABC):
    @staticmethod
    @abstractmethod
    def attack() -> int:
        raise NotImplementedError
    
class SwordAttack(AttackStrategy):
    @staticmethod
    def attack():
        return random.choice([4, 5, 6])

class MagicalAttack(AttackStrategy):
    @staticmethod
    def attack():
        return random.choice([1, 2, 3, 7, 8, 9])
    
class AxeAttack(AttackStrategy):
    @staticmethod
    def attack():
        return random.choice([0, 0, 0, 7, 8, 9])

class Character:
    def __init__(self, role: Role, attack: AttackStrategy.attack, health: int):
        self.role = role
        self.health = health
        self.attack = attack

class CardGame(ABC):
    def __init__(self, players: List[Character]):
        self.players = players

    def combat(self, p1_index: int, p2_index: int) -> int:
        """
        Returns -1 if both players alive or both dead after combat, otherwise, returns the index of 
        the winning player
        """
        p1: Character = self.players[p1_index]
        p2: Character = self.players[p2_index]

        all_matchups: Dict[bool, tuple] = {0: (p1_index, p2_index), 1: (p2_index, p1_index)}
        turns: int = 10
        p1_is_attacking: int = turns % 2
        while turns > 0:
            matchup: Tuple[int] = all_matchups[0] if p1_is_attacking else all_matchups[1]
            attacker: Character = self.players[matchup[0]]
            defender: Character = self.players[matchup[1]]
            print(f"{attacker.role.value} vs. {defender.role.value}")

            self.hit(attacker, defender)
            if defender.health <= 0:
                print(f"{defender.role.value} loses, game over!")
                break
            turns -= 1
            p1_is_attacking = turns % 2
            print('-'*10)

        p1_is_alive: bool = p1.health > 0
        p2_is_alive: bool = p2.health > 0
        if p1_is_alive == p2_is_alive:
            return -1
        return p1_index if p1_is_alive else p2_index
    
    @abstractmethod
    def hit(self, attacker: Character, defender: Character) -> None:
        raise NotImplementedError
    
class TemporaryDamageCardGame(CardGame):
    def hit(self, attacker: Character, defender: Character) -> None:
        health: int = defender.health
        defender.health -= attacker.attack()
        if defender.health > 0:
            defender.health = health

class PermanentDamageCardGame(CardGame):
    def hit(self, attacker: Character, defender: Character) -> None:
        attack: int = attacker.attack()
        print(f"Defender's health: {defender.health}")
        print(f"Attacker's attack: {attack}")
        defender.health -= attack
        print(f"After being attacked, defender's health: {defender.health}")


def temporary_cardgame_test_drive():
    p1: Character = Character(Role.SWORDSMAN, SwordAttack.attack, 8)
    p2: Character = Character(Role.MAGE, MagicalAttack.attack, 6)

    game: CardGame = TemporaryDamageCardGame([p1, p2])
    winner: Character = game.players[game.combat(0, 1)]
    ic(winner.role.value)

def permanent_cardgame_test_drive():
    p1: Character = Character(Role.ARCHER, AxeAttack.attack, 35)
    p2: Character = Character(Role.MAGE, MagicalAttack.attack, 25)

    game: CardGame = PermanentDamageCardGame([p1, p2])
    winner: Character = game.players[game.combat(0, 1)]
    ic(winner.role.value)

if __name__ == "__main__":
    # temporary_cardgame_test_drive()
    permanent_cardgame_test_drive()