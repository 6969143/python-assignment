class BankAccount:
    total_accounts = 0
    
    def __init__(self, owner, balance=0.0):
        self.owner = owner
        self.__balance = balance
        BankAccount.total_accounts += 1
    
    def deposit(self, amt):
        if amt > 0:
            self.__balance += amt
    
    def withdraw(self, amt):
        if 0 < amt <= self.__balance:
            self.__balance -= amt
    
    @property
    def balance(self):
        return self.__balance
    
    def __str__(self):
        return f"BankAccount(owner={self.owner}, balance={self.__balance})"
    
    def __add__(self, other):
        new_owner = f"{self.owner} {other.owner}"
        return BankAccount(new_owner, self.__balance + other.__balance)


class SavingsAccount(BankAccount):
    def __init__(self, owner, balance=0.0, rate=0.02):
        super().__init__(owner, balance)
        self.rate = rate
    
    def apply_interest(self):
        self.deposit(self.balance * self.rate)


class CheckingAccount(BankAccount):
    def __init__(self, owner, balance=0.0, limit=100):
        super().__init__(owner, balance)
        self.limit = limit
    
    def withdraw(self, amt):
        if amt > 0 and amt <= self.balance + self.limit:
            self._BankAccount__balance -= amt


class Customer:
    def __init__(self, name):
        self.name = name
        self.accounts = []
    
    def add_account(self, account):
        self.accounts.append(account)
    
    def total_balance(self):
        return sum(acc.balance for acc in self.accounts)


def print_account_summary(obj):
    print(f"Owner: {obj.owner}, Balance: ${obj.balance}")
