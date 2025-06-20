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
