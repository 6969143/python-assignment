# class BankAccount:
#     total_accounts = 0
    
#     def __init__(self, owner, balance=0.0):
#         self.owner = owner
#         self.__balance = balance
#         BankAccount.total_accounts += 1
    
#     def deposit(self, amt):
#         if amt <= 0:
#             raise ValueError("Amount must be positive")
#         self.__balance += amt
    
#     def withdraw(self, amt):
#         if amt <= 0 or amt > self.__balance:
#             raise ValueError("Invalid withdrawal amount")
#         self.__balance -= amt
    
#     @property
#     def balance(self):
#         return self.__balance
    
#     @balance.setter
#     def balance(self, value):
#         if value < 0:
#             raise ValueError("Balance cannot be negative")
#         self.__balance = value
    
#     def __str__(self):
#         return f"BankAccount(owner={self.owner}, balance={self.__balance})"
    
#     def __repr__(self):
#         return f"BankAccount(owner='{self.owner}', balance={self.__balance}, total_accounts={BankAccount.total_accounts})"
    
#     def __add__(self, other):
#         if not isinstance(other, BankAccount):
#             raise TypeError("Can only add BankAccount objects")
#         new_owner = f"{self.owner} {other.owner}"
#         new_balance = self.__balance + other.balance
#         BankAccount.total_accounts -= 1
#         return BankAccount(new_owner, new_balance)


# class SavingsAccount(BankAccount):
#     def __init__(self, owner, balance=0.0, interest_rate=0.02):
#         super().__init__(owner, balance)
#         self.interest_rate = interest_rate
    
#     def apply_interest(self):
#         interest = self.balance * self.interest_rate
#         self.deposit(interest)


# class CheckingAccount(BankAccount):
#     def __init__(self, owner, balance=0.0, overdraft_limit=100.0):
#         super().__init__(owner, balance)
#         self._overdraft_limit = overdraft_limit
    
#     def withdraw(self, amt):
#         if amt <= 0:
#             raise ValueError("Amount must be positive")
#         if amt > self.balance + self._overdraft_limit:
#             raise ValueError("Exceeds overdraft limit")
#         self._BankAccount__balance -= amt
    
#     @property
#     def overdraft_limit(self):
#         return self._overdraft_limit
    
#     @overdraft_limit.setter
#     def overdraft_limit(self, value):
#         if value < 0:
#             raise ValueError("Overdraft limit cannot be negative")
#         self._overdraft_limit = value


# class Customer:
#     def __init__(self, name):
#         self.name = name
#         self.accounts = []
    
#     def add_account(self, account):
#         self.accounts.append(account)
    
#     def total_balance(self):
#         return sum(acc.balance for acc in self.accounts)
    
#     def transfer(self, from_acc, to_acc, amt):
#         from_acc.withdraw(amt)
#         to_acc.deposit(amt)


# class MockAccount:
#     def __init__(self, owner, balance):
#         self.owner = owner
#         self._balance = balance
    
#     def get_balance(self):
#         return self._balance
    
#     @property
#     def balance(self):
#         return self._balance


# def print_account_summary(obj):
#     balance = obj.balance if hasattr(obj, 'balance') else obj.get_balance()
#     print(f"Account Summary: Owner={obj.owner}, Balance=${balance:.2f}")


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