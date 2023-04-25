from abc import ABC, abstractmethod

class Account(ABC):
    def __init__(self, balance=0):
        self.balance = balance

    @abstractmethod
    def deposit(self, amount):
        pass

    @abstractmethod
    def withdraw(self, amount):
        pass


class CheckingAccount(Account):
    def __init__(self, balance=0):
        super().__init__(balance)

    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        if self.balance - amount >= 0:
            self.balance -= amount
        else:
            print("Insufficient funds")


class SavingsAccount(Account):
    def __init__(self, balance=0):
        super().__init__(balance)

    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        if self.balance - amount >= 0:
            self.balance -= amount
        else:
            print("Insufficient funds")


class BusinessAccount(Account):
    def __init__(self, balance=0):
        super().__init__(balance)

    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        if self.balance - amount >= 0:
            self.balance -= amount
        else:
            print("Insufficient funds")


class ATM:
    def __init__(self):
        self.accounts = {}

    def create_account(self, account_type, account_number, balance=0):
        if account_type == "checking":
            self.accounts[account_number] = CheckingAccount(balance)
        elif account_type == "savings":
            self.accounts[account_number] = SavingsAccount(balance)
        elif account_type == "business":
            self.accounts[account_number] = BusinessAccount(balance)
        else:
            print("Invalid account type")

    def deposit(self, account_number, amount):
        if account_number in self.accounts:
            self.accounts[account_number].deposit(amount)
        else:
            print("Account not found")

    def withdraw(self, account_number, amount):
        if account_number in self.accounts:
            self.accounts[account_number].withdraw(amount)
        else:
            print("Account not found")

    def check_balance(self, account_number):
        if account_number in self.accounts:
            print(f"Account balance: {self.accounts[account_number].balance}")
        else:
            print("Account not found")

atm = ATM()
atm.create_account("checking", "123456", 1000)
atm.deposit("123456", 500)
atm.withdraw("123456", 200)
atm.check_balance("123456")