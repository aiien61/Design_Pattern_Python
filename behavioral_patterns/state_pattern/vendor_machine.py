from abc import ABC, abstractmethod

class GumballMachine:
    def __init__(self, number_gumballs: int):
        self.no_coin_state = NoCoinState(self)
        self.sold_out_state = SoldOutState(self)
        self.has_coin_state = HasCoinState(self)
        self.sold_state = SoldState(self)
        self.count = number_gumballs
        self.state = self.no_coin_state if number_gumballs > 0 else self.sold_out_state

    def insert_coin(self):
        self.state.insert_coin()

    def eject_coin(self):
        self.state.eject_coin()

    def turn_crank(self):
        self.state.turn_crank()
        self.state.dispense()

    def release_ball(self):
        print("A gumball comes rolling out the slot...")
        if self.count > 0:
            self.count -= 1
    
    def refill(self, count: int):
        self.count += count
        print(f"The gumball machine was just refilled; its new count is: {self.count}")
        self.state.refill()

    def set_state(self, state):
        self.state = state

    def __repr__(self) -> str:
        result = []
        result.append("\nMighty Gumball, Inc.")
        result.append("\nGumball Model #1005")
        result.append(f"\nInventory: {self.count} gumball")
        if self.count != 1:
            result.append("s")
        
        result.append("\n")
        result.append(f"Machine is {self.state}\n")
        return "".join(result)

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

class NoCoinState(State):
    def __init__(self, gumball_machine: GumballMachine):
        self.gumball_machine = gumball_machine

    def insert_coin(self):
        print('You inserted a coin')
        self.gumball_machine.set_state(self.gumball_machine.has_coin_state)
    
    def eject_coin(self):
        print("You haven't inserted a coin")

    def turn_crank(self):
        print("You turned, but there's no coin")

    def dispense(self):
        print("YOu need to pay first")

    def refill(self):
        raise NotImplementedError
    
    def __repr__(self):
        return "waiting for a coin"
    
class SoldOutState(State):
    def __init__(self, gumball_machine: GumballMachine):
        self.gumball_machine = gumball_machine

    def insert_coin(self):
        print("You can't insert a coin, the machine is sold out")

    def eject_coin(self):
        print("You can't eject, you haven't inserted a coin yet")

    def turn_crank(self):
        print("You turned, but there are no gumballs")

    def dispense(self):
        print("No gumball dispensed")

    def refill(self):
        self.gumball_machine.set_state(self.gumball_machine.no_coin_state)
    
    def __repr__(self):
        return "sold out"

class HasCoinState(State):
    def __init__(self, gumball_machine: GumballMachine):
        self.gumball_machine = gumball_machine

    def insert_coin(self):
        print("You can't insert another coin")

    def eject_coin(self):
        print("Coin returned")
        self.gumball_machine.set_state(self.gumball_machine.no_coin_state)

    def turn_crank(self):
        print("You turned...")
        self.gumball_machine.set_state(self.gumball_machine.sold_state)

    def dispense(self):
        print("No gumball dispensed")

    def refill(self):
        raise NotImplementedError

    def __repr__(self):
        return "waiting for turn of crank"

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
        if self.gumball_machine.count > 0:
            self.gumball_machine.set_state(self.gumball_machine.no_coin_state)
        else:
            self.gumball_machine.set_state(self.gumball_machine.sold_out_state)

    def refill(self):
        raise NotImplementedError

    def __repr__(self):
        return "dispensing a gumball"

def gumball_machine_test_drive():
    gumball_machine = GumballMachine(2)
    print(gumball_machine)
    gumball_machine.insert_coin()
    gumball_machine.turn_crank()

    print(gumball_machine)

    gumball_machine.insert_coin()
    gumball_machine.turn_crank()
    gumball_machine.insert_coin()
    gumball_machine.turn_crank()

    gumball_machine.refill(5)
    gumball_machine.insert_coin()
    gumball_machine.turn_crank()

    print(gumball_machine)

if __name__ == "__main__":
    gumball_machine_test_drive()