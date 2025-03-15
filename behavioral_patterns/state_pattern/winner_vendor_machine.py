from abc import ABC, abstractmethod
from datetime import datetime
from typing import List
from rich import print
from icecream import ic
import random

class State(ABC):
    @abstractmethod
    def insert_coin(self): raise NotImplementedError
    
    @abstractmethod
    def eject_coin(self): raise NotImplementedError
    
    @abstractmethod
    def turn_crank(self): raise NotImplementedError
    
    @abstractmethod
    def dispense(self): raise NotImplementedError
    
    @abstractmethod
    def refill(self): raise NotImplementedError


class StringBuffer:
    def __init__(self):
        self.ls: List[str] = []
    
    def append(self, string: str):
        self.ls.append(string)

    def __str__(self) -> str:
        return ''.join(self.ls)


class GumballMachine:
    def __init__(self, number_of_gumballs: int):
        self.sold_out_state: State = SoldOutState(self)
        self.no_coin_state: State = NoCoinState(self)
        self.has_coin_state: State = HasCoinState(self)
        self.sold_state: State = SoldState(self)
        self.winner_state = WinnerState(self)

        self.count: int = number_of_gumballs
        if number_of_gumballs > 0:
            self.state = self.no_coin_state

    def insert_coin(self):
        self.state.insert_coin()

    def eject_coin(self):
        self.state.eject_coin()

    def turn_crank(self):
        self.state.turn_crank()
        self.state.dispense()

    def set_state(self, state: State):
        self.state = state

    def release_ball(self):
        print("A gumball comes rolling out the slot...")
        if self.count > 0:
            self.count -= 1

    def get_count(self):
        return self.count
    
    def refill(self, count: int):
        self.count += count
        print(f"The gumball machine was just refilled; its new count is: {self.count}")
        self.state.refill()

    def get_state(self) -> State:
        return self.state
    
    def get_sold_out_state(self) -> State:
        return self.sold_out_state
    
    def get_no_coin_state(self) -> State:
        return self.no_coin_state
    
    def get_has_coin_state(self) -> State:
        return self.has_coin_state
    
    def get_sold_state(self) -> State:
        return self.sold_state
    
    def get_winner_state(self) -> State:
        return self.winner_state
    
    def __str__(self) -> str:
        result: StringBuffer = StringBuffer()
        result.append("\nMighty Gumball, Inc.")
        result.append("\nGumball Model #1005")
        result.append(f"\nInventory: {self.count} gumball")
        if self.count != 1:
            result.append("s")

        result.append("\n")
        result.append(f"Machine is {self.state}\n")
        return str(result)
    
    def __repr__(self) -> str:
        return str(self)


class NoCoinState(State):
    def __init__(self, gumball_machine: GumballMachine):
        self.gumball_machine = gumball_machine

    def insert_coin(self):
        print("You inserted a coin")
        self.gumball_machine.set_state(self.gumball_machine.get_has_coin_state())
    
    def eject_coin(self):
        print("You haven't inserted a coin")

    def turn_crank(self):
        print("You turned, but there's no coin")

    def dispense(self):
        print("You need to pay first")
    
    def refill(self):
        raise NotImplementedError
    
    def __str__(self) -> str:
        return "waiting for a coin"
    
    def __repr__(self) -> str:
        return str(self)


class HasCoinState(State):
    random_winner: random = random
    random_winner.seed(datetime.now().strftime(".%f")[1:4])

    def __init__(self, gumball_machine: GumballMachine):
        self.gumball_machine = gumball_machine

    def insert_coin(self):
        print("You can't insert another coin")
    
    def eject_coin(self):
        print('Coin returned')
        self.gumball_machine.set_state(self.gumball_machine.get_no_coin_state())
    
    def turn_crank(self):
        print("You turned...")
        winner: int = self.random_winner.randint(0, 9)
        if winner == 0 and self.gumball_machine.get_count() > 1:
            self.gumball_machine.set_state(self.gumball_machine.get_winner_state())
        else:
            self.gumball_machine.set_state(self.gumball_machine.get_sold_state())
    
    def dispense(self):
        print("No gumball dispensed")

    def refill(self):
        raise NotImplementedError
    
    def __str__(self) -> str:
        return "waiting for turn of crank"

    def __repr__(self) -> str:
        return str(self)


class SoldState(State):
    def __init__(self, gumball_machine: GumballMachine):
        self.gumball_machine = gumball_machine

    def insert_coin(self):
        print("Please wait, we're already giving you a gumball")

    def eject_coin(self):
        print("Sorry, you already turned the crank")

    def turn_crank(self):
        print("Turning twice doesn't get you another gumball")

    def dispense(self):
        self.gumball_machine.release_ball()
        if self.gumball_machine.get_count() > 0:
            self.gumball_machine.set_state(self.gumball_machine.get_no_coin_state())
        else:
            print("Oops, out of gumballs")
            self.gumball_machine.set_state(self.gumball_machine.get_sold_out_state())
    
    def refill(self):
        raise NotImplementedError

    def __str__(self) -> str:
        return "dispensing a gumball"

    def __repr__(self) -> str:
        return str(self)


class SoldOutState(State):
    def __init__(self, gumball_machine: GumballMachine):
        self.gumball_machine = gumball_machine

    def insert_coin(self):
        print("You can't isnert a coin, the machine is sold out")

    def eject_coin(self):
        print("You can't eject, you haven't inserted a coin yet")

    def turn_crank(self):
        print("You turned, but there are no gumballs")

    def dispense(self):
        print("No gumball dispensed")

    def refill(self):
        self.gumball_machine.set_state(self.gumball_machine.get_no_coin_state())
    
    def __str__(self) -> str:
        return "sold out"

    def __repr__(self) -> str:
        return str(self)


class WinnerState(State):
    def __init__(self, gumball_machine: GumballMachine):
        self.gumball_machine = gumball_machine

    def insert_coin(self):
        print("Please wait, we're already giving you a Gumball")

    def eject_coin(self):
        print("Please wait, we're already giving you a Gumball")

    def turn_crank(self):
        print("Turning again doesn't get you another gumball")

    def dispense(self):
        self.gumball_machine.release_ball()
        if self.gumball_machine.get_count() == 0:
            self.gumball_machine.set_state(self.gumball_machine.get_sold_out_state())
        else:
            self.gumball_machine.release_ball()
            print("YOU'RE A WINNER! You got two gumballs for you coin")
            if self.gumball_machine.get_count() > 0:
                self.gumball_machine.set_state(self.gumball_machine.get_no_coin_state())
            else:
                print("Oops, out of gumballs")
                self.gumball_machine.set_state(self.gumball_machine.get_sold_out_state())
    
    def refill(self):
        raise NotImplementedError
    
    def __str__(self) -> str:
        return "dispensing two gumballs for you coin, because YOU'RE A WINNER"

    def __repr__(self) -> str:
        return str(self)


class GumballMachineTestDrive:
    @staticmethod
    def main(*args):
        gumball_mahcine: GumballMachine = GumballMachine(10)
        ic(gumball_mahcine)

        for _ in range(10):
            gumball_mahcine.insert_coin()
            gumball_mahcine.turn_crank()

            ic(gumball_mahcine)
            print("------------------")
            if gumball_mahcine.get_count() == 0:
                break
        
        gumball_mahcine.refill(10)
        ic(gumball_mahcine)

if __name__ == "__main__":
    GumballMachineTestDrive.main()
