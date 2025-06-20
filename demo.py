# from banking import BankAccount, SavingsAccount, CheckingAccount, Customer, MockAccount, print_account_summary

# def main():
    
#     acc1 = BankAccount("Alice", 1000)
#     acc2 = BankAccount("Bob", 500)
#     print(f"Created: {acc1}")
#     print(f"Created: {acc2}")
#     print(f"Total accounts: {BankAccount.total_accounts}\n")
    
#     acc1.deposit(200)
#     print(f"After deposit: {acc1}")
#     acc1.withdraw(150)
#     print(f"After withdrawal: {acc1}\n")
    
#     savings = SavingsAccount("Charlie", 2000, 0.05)
#     checking = CheckingAccount("David", 800, 200)
#     print(f"Savings: {savings}")
#     print(f"Checking: {checking}\n")
    
#     print(f"Savings before interest: ${savings.balance}")
#     savings.apply_interest()
#     print(f"Savings after interest: ${savings.balance}\n")
    
#     print(f"Checking balance: ${checking.balance}")
#     print(f"Overdraft limit: ${checking.overdraft_limit}")
#     checking.withdraw(900)
#     print(f"After overdraft withdrawal: ${checking.balance}\n")
    
#     accounts = [savings, checking]
#     for acc in accounts:
#         print(f"Processing {type(acc).__name__}: {acc.owner}")
#         if hasattr(acc, 'apply_interest'):
#             acc.apply_interest()
#             print(f"  Applied interest, new balance: ${acc.balance}")
#         else:
#             print(f"  Current balance: ${acc.balance}")
#     print()
    
#     new_acc1 = BankAccount("Emma", 300)
#     new_acc2 = BankAccount("Frank", 700)
#     merged = new_acc1 + new_acc2
#     print(f"Merged account: {merged}")
#     print(f"Total accounts after merge: {BankAccount.total_accounts}\n")
    
#     customer = Customer("John Doe")
#     customer.add_account(acc1)
#     customer.add_account(savings)
#     print(f"Customer: {customer.name}")
#     print(f"Total balance across accounts: ${customer.total_balance():.2f}")
    
#     print("9. Transfer between accounts:")
#     print(f"Before transfer - Account 1: ${acc1.balance}, Savings: ${savings.balance}")
#     customer.transfer(acc1, savings, 100)
#     print(f"After transfer - Account 1: ${acc1.balance}, Savings: ${savings.balance}\n")
    
#     mock_acc = MockAccount("TestUser", 1500)
#     all_objects = [acc1, savings, checking, mock_acc]
    
#     for obj in all_objects:
#         print_account_summary(obj)
#     print()
    
#     print("__str__ representations:")
#     for acc in [acc1, savings, checking]:
#         print(f"  {acc}")
    
#     print("\n__repr__ representations:")
#     for acc in [acc1, savings, checking]:
#         print(f"  {repr(acc)}")

# if __name__ == "__main__":
#     main()

from banking import BankAccount, SavingsAccount, CheckingAccount, Customer, print_account_summary

acc1 = BankAccount("Alice", 1000)
acc2 = BankAccount("Bob", 500)

acc1.deposit(200)
acc1.withdraw(150)

savings = SavingsAccount("Charlie", 2000, 0.05)
checking = CheckingAccount("David", 800, 200)

savings.apply_interest()

checking.withdraw(900)

accounts = [savings, checking]
for acc in accounts:
    if hasattr(acc, 'apply_interest'):
        acc.apply_interest()

merged = acc1 + acc2

customer = Customer("John")
customer.add_account(acc1)
customer.add_account(savings)

print(f"Customer total: ${customer.total_balance()}")

for acc in [acc1, savings, checking]:
    print_account_summary(acc)
    print(acc)