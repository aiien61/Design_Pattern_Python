"""
Imagine a game where one or more rats can attack a player. Each individual rat has an initial attack 
value of 1. However, rats attack as a swarm, so each rat's attack value is actually equal to the 
total number of rats in play.

Given that a rat enters play through the initializer and leaves play (dies) via its __exit__ method,
please implement the Game and Rat classes so that, at any point in the game, the Attack value of a 
rat is always consistent.
"""
import unittest
from typing import Any


class Event(list):
    def __call__(self, *args: Any, **kwargs: Any) -> Any:
        for item in self:
            item(*args, **kwargs)


class Game:
    def __init__(self):
        self.has_rat_in: Event = Event()
        self.has_rat_out: Event = Event()
        self.ally_new_rat: Event = Event()


class Rat:
    def __init__(self, game: Game):
        self.game: Game = game
        self.attack: int = 1
        game.has_rat_in.append(self.has_rat_in)
        game.has_rat_out.append(self.has_rat_out)
        game.ally_new_rat.append(self.ally_new_rat)
        
        self.game.has_rat_in(self)

    def has_rat_in(self, new_rat: 'Rat') -> None:
        if self != new_rat:
            self.attack += 1
            self.game.ally_new_rat(new_rat)
        return None
    
    
    def has_rat_out(self) -> None:
        self.attack -= 1
        return None

    
    def ally_new_rat(self, new_rat: 'Rat'):
        if self == new_rat:
            self.attack += 1


    def __enter__(self):
        return self

    def __exit__(self, *args, **kwargs):
        self.game.has_rat_in.remove(self.has_rat_in)
        self.game.has_rat_out.remove(self.has_rat_out)
        self.game.ally_new_rat.remove(self.ally_new_rat)
        self.game.has_rat_out()


class Evaluate(unittest.TestCase):
    def test_single_rat(self):
        game = Game()
        rat = Rat(game)
        self.assertEqual(1, rat.attack)

    def test_two_rats(self):
        game = Game()
        rat = Rat(game)
        rat2 = Rat(game)
        self.assertEqual(2, rat.attack)
        self.assertEqual(2, rat2.attack)

    def test_three_rats_one_dies(self):
        game = Game()

        rat = Rat(game)
        self.assertEqual(1, rat.attack)

        rat2 = Rat(game)
        self.assertEqual(2, rat.attack)
        self.assertEqual(2, rat2.attack)

        with Rat(game) as rat3:
            self.assertEqual(3, rat.attack)
            self.assertEqual(3, rat2.attack)
            self.assertEqual(3, rat3.attack)

        self.assertEqual(2, rat.attack)
        self.assertEqual(2, rat2.attack)

    def test_four_rats_one_dies(self):
        game = Game()

        rat = Rat(game)
        self.assertEqual(1, rat.attack)

        rat2 = Rat(game)
        self.assertEqual(2, rat.attack)
        self.assertEqual(2, rat2.attack)

        with Rat(game) as rat3:
            self.assertEqual(3, rat.attack)
            self.assertEqual(3, rat2.attack)
            self.assertEqual(3, rat3.attack)

        self.assertEqual(2, rat.attack)
        self.assertEqual(2, rat2.attack)

        rat4 = Rat(game)
        self.assertEqual(3, rat.attack)
        self.assertEqual(3, rat2.attack)
        self.assertEqual(3, rat4.attack)



if __name__ == '__main__':
    unittest.main()