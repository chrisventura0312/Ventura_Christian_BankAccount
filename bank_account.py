class BankAccount:
    accounts = []

    def __init__(self, interest_rate=0, balance=0):
        self.interest_rate = interest_rate
        self.balance = balance
        BankAccount.accounts.append(self)

    def deposit(self, amount):
        self.balance += amount
        return self

    def withdraw(self, amount):
        if self.balance >= amount:
            self.balance -= amount
        else:
            print("Insufficient funds: Charging a $5 fee")
            self.balance -= 5
        return self

    def display_account_info(self):
        print(f"Balance: ${self.balance}")
        return self

    def yield_interest(self):
        self.balance += self.balance * self.interest_rate
        return self

    @classmethod
    def print_all_accounts(cls):
        for account in cls.accounts:
            print(f"Interest rate: {account.interest_rate}, Balance: ${account.balance}")

# create accounts
account1 = BankAccount(0.02, 1000)
account2 = BankAccount(0.03, 500)
account3 = BankAccount(0.01, 2000)

# chain deposit, withdraw, yield_interest and display_account_info methods for account1
account1.deposit(100).deposit(200).deposit(300).withdraw(400).yield_interest().display_account_info()

# chain deposit, withdraw, yield_interest and display_account_info methods for account2
account2.deposit(50).deposit(100).withdraw(200).withdraw(150).withdraw(100).withdraw(50).yield_interest().display_account_info()

account3.yield_interest().deposit(1000).yield_interest().display_account_info()
# print all accounts' info
BankAccount.print_all_accounts()
