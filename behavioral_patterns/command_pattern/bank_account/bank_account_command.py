from typing import Final
from abc import ABC, abstractmethod
from enum import Enum, auto
from icecream import ic


class BankAccount:
    """Receiver"""

    OVERDRAFT_LIMIT: Final[int] = -500

    def __init__(self, balance: int=0):
        self.balance = balance

    def deposit(self, amount: int) -> bool:
        self.balance += amount
        print(f'Deposited {amount}, balance = {self.balance}')
        return True
    
    def withdraw(self, amount: int) -> bool:
        if (self.balance - amount) >= self.OVERDRAFT_LIMIT:
            self.balance -= amount
            print(f'Withdraw {amount}, balance = {self.balance}')
            return True
        return False
    
    def __repr__(self):
        return f"Balance = {self.balance}"
    

class Command(ABC):
    @abstractmethod
    def invoke(self):
        raise NotImplementedError
    
    @abstractmethod
    def undo(self):
        raise NotImplementedError
    

class BankAction(Enum):
    DEPOSIT = auto()
    WITHDRAW = auto()


class BankAccountDepositCommand(Command):
    success: bool

    def __init__(self, account: BankAccount, amount: int):
        self.amount = amount
        self.account = account

    def invoke(self) -> bool:
        self.success = self.account.deposit(self.amount)
        return self.success
    
    def undo(self) -> bool:
        if not self.success:
            return False        
        self.account.withdraw(self.amount)
        return self.success

class BankAccountWithdrawCommand(Command):
    success: bool

    def __init__(self, account: BankAccount, amount: int):
        self.amount = amount
        self.account = account

    def invoke(self) -> bool:
        self.success = self.account.withdraw(self.amount)
        return self.success

    def undo(self) -> bool:
        if not self.success:
            return False
        self.account.deposit(self.amount)
        return self.success


class AutomatedTellerMachine:
    def __init__(self, account: BankAccount):
        self.account = account
        self.command = None
        

    def set_command(self, command: Command) -> bool:
        self.command = command
        return True
            

    def deposit_button_being_pushed(self, amount: int) -> bool:
        self.set_command(command=BankAccountDepositCommand(account=self.account, amount=amount))
        success: bool = self.command.invoke()
        return success
    
    def withdraw_button_being_pushed(self, amount: int) -> bool:
        self.set_command(command=BankAccountWithdrawCommand(account=self.account, amount=amount))
        success: bool = self.command.invoke()
        return success
    
    def undo_button_being_pushed(self) -> bool:
        if self.command is None:
            return False
        success: bool = self.command.undo()
        return success

if __name__ == '__main__':
    new_account = BankAccount()
    ic(new_account)

    atm = AutomatedTellerMachine(new_account)
    atm.deposit_button_being_pushed(amount=100)
    ic('After $100 deposit:', new_account)
    atm.undo_button_being_pushed()
    ic('$100 deposit undone:', new_account)

    atm.withdraw_button_being_pushed(amount=1_000)
    ic('After impossible withdrawal:', new_account)
    atm.undo_button_being_pushed()
    ic('After undo:', new_account)
