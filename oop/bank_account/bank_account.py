class BankAccount:
    # don't forget to add some default values for these parameters!
    bank_name = "The Dojo Bank"
    all_accounts = []

    def __init__(self, int_rate, balance):
        # your code here! (remember, instance attributes go here)
        self.int_rate = int_rate
        self.balance = balance
        BankAccount.all_accounts.append(self)
        # don't worry about user info here; we'll involve the User class soon

    def deposit(self, amount):
        # your code here
        self.amount = amount
        self.balance = self.amount + self.balance
        return self

    def withdraw(self, amount):
        # your code here
        self.amount = amount
        if self.balance >= self.amount:
            self.balance = self.balance - self.amount
        else:
            self.balance = self.balance - 5
            print("Insufficient funds: Charging a $5 fee")
        return self

    def display_account_info(self):
        # your code here
        print(f"Balance is {self.balance}")
        return self

    def yield_interest(self):
        # your code here
        if self.balance > 0:
            self.balance = self.balance + (self.balance * self.int_rate)
        else:
            self.balance = self.balance
        return self

    @classmethod
    def all_balances(cls):
        for account in cls.all_accounts:
            # print(account.balance)
            account.display_account_info()

# Create 2 accounts
naruto = BankAccount(.03, 100)
sasuke = BankAccount(.02, 100)

# To the first account, make 3 deposits and 1 withdrawal, then yield interest and display the account's info all in one line of code (i.e. chaining)
naruto.deposit(200).deposit(200).deposit(500).withdraw(200).yield_interest().display_account_info()

# To the second account, make 2 deposits and 4 withdrawals, then yield interest and display the account's info all in one line of code (i.e. chaining)
sasuke.deposit(200).deposit(400).withdraw(50).withdraw(150).withdraw(50).withdraw(100).yield_interest().display_account_info()

BankAccount.all_balances()