from typing import Final, List, Deque
from abc import ABC, abstractmethod
from collections import deque
from enum import Enum, auto
from icecream import ic
import unittest


class BankAccount:
    """Receiver"""

    OVERDRAFT_LIMIT: Final[int] = -500

    def __init__(self, account_number: str, balance: int = 0):
        self.balance = balance
        self.account_number = account_number

    def deposit(self, amount: int) -> bool:
        self.balance += amount
        print(f'Deposited {amount} to {self.account_number}, balance = {self.balance}')
        return True

    def withdraw(self, amount: int) -> bool:
        if (self.balance - amount) >= self.OVERDRAFT_LIMIT:
            self.balance -= amount
            print(f'Withdraw {amount} from {self.account_number}, balance = {self.balance}')
            return True
        return False

    def __repr__(self):
        return f"Account:{self.account_number}, Balance = {self.balance}"


class Command(ABC):
    success: bool

    @abstractmethod
    def invoke(self):
        raise NotImplementedError

    @abstractmethod
    def undo(self):
        raise NotImplementedError


class NoCommand(Command):
    def invoke(self): pass
    def undo(self): pass


class BankAction(Enum):
    DEPOSIT = auto()
    WITHDRAW = auto()


class BankAccountDepositCommand(Command):
    success: bool

    def __init__(self, account: BankAccount, amount: int):
        self.amount = amount
        self.account = account
        self.success = None

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
        self.success = None

    def invoke(self) -> bool:
        self.success = self.account.withdraw(self.amount)
        return self.success

    def undo(self) -> bool:
        if not self.success:
            return False
        self.account.deposit(self.amount)
        return self.success
    
class MacroBankAccountCommand(Command):
    success: bool
    restored_queue: Deque[Command]

    def __init__(self, commands: List[Command]):
        self.commands = commands
        self.success = None
        self.restored_queue = deque([])

    def invoke(self) -> bool:
        for command in self.commands:
            self.success = command.invoke()
            if self.success:
                self.restored_queue.append(command)
            else:
                self.undo()
                return False
        return self.success

    def undo(self) -> bool:
        while self.restored_queue:
            command = self.restored_queue.popleft()
            command.undo()
        return True


class MoneyTransferCommand(Command):
    success: bool
    restored_queue: Deque[Command]

    def __init__(self, from_account: BankAccount, to_account: BankAccount, amount: int):
        self.success = None
        self.commands: List[Command] = []
        self.commands.append(BankAccountWithdrawCommand(account=from_account, amount=amount))
        self.commands.append(BankAccountDepositCommand(account=to_account, amount=amount))
        self.transfer_command: Command = MacroBankAccountCommand(self.commands)

    def invoke(self) -> bool:
        self.success = self.transfer_command.invoke()
        return self.success
    
    def undo(self) -> bool:
        self.success = self.transfer_command.undo() if self.transfer_command.restored_queue else False
        return self.success


class TestSuite(unittest.TestCase):
    def test_composite_commands_when_multiple_deposits(self):
        new_account = BankAccount(account_number='0001')
        deposit1 = BankAccountDepositCommand(new_account, 1_000)
        deposit2 = BankAccountDepositCommand(new_account, 1_000)
        composite = MacroBankAccountCommand([deposit1, deposit2])
        composite.invoke()

        actual = new_account.balance
        expected = 2_000
        self.assertEqual(actual, expected)

    def test_composite_commands_when_undo_multiple_deposits(self):
        new_account = BankAccount(account_number='0002')
        deposit1 = BankAccountDepositCommand(new_account, 1_000)
        deposit2 = BankAccountDepositCommand(new_account, 1_000)
        composite = MacroBankAccountCommand([deposit1, deposit2])
        composite.invoke()
        composite.undo()

        actual = new_account.balance
        expected = 0
        self.assertEqual(actual, expected)

    def test_composite_deposit_when_restore_partial_commands(self):
        new_account = BankAccount(account_number='0003')
        actions: List[Command] = []
        actions.append(BankAccountDepositCommand(new_account, 1_000))
        actions.append(BankAccountDepositCommand(new_account, 1_000))
        actions.append(BankAccountWithdrawCommand(new_account, 3_000))
        actions.append(BankAccountDepositCommand(new_account, 1_000))
        composite = MacroBankAccountCommand(actions)
        composite.invoke()
        actual = new_account.balance
        expected = 0
        self.assertEqual(actual, expected)

    def test_transfer_success(self):
        acct1 = BankAccount(account_number='0004', balance=100)
        acct2 = BankAccount(account_number='0005')

        transfer = MoneyTransferCommand(acct1, acct2, 100)
        transfer.invoke()

        actual = (acct1.balance, acct2.balance)
        expected = (0, 100)
        self.assertEqual(actual, expected)

    def test_transfer_fail(self):
        acct1 = BankAccount(account_number='0006', balance=100)
        acct2 = BankAccount(account_number='0007')

        transfer = MoneyTransferCommand(acct1, acct2, 1_000)
        transfer.invoke()
        ic(acct1)
        ic(acct2)

        actual = (acct1.balance, acct2.balance)
        expected = (100, 0)
        self.assertEqual(actual, expected)


if __name__ == '__main__':
    unittest.main()