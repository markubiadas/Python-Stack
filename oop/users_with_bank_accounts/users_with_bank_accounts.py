class BankAccount:
    # don't forget to add some default values for these parameters!
    bank_name = "The Dojo Bank"

    def __init__(self, int_rate, balance):
        # your code here! (remember, instance attributes go here)
        self.int_rate = int_rate
        self.balance = balance
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


class User:
    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.account = BankAccount(int_rate=0.02, balance=0)

    # other methods

    def make_deposit(self, amount):
        self.amount = amount
        self.account.balance = self.account.balance + self.amount
        return self

    def make_withdraw(self, amount):
        self.amount = amount
        if self.account.balance >= self.amount:
            self.account.balance = self.account.balance - self.amount
        else:
            self.account.balance = self.account.balance - 5
            print("Insufficient funds: Charging a $5 fee")
        return self

    def display_user_balance(self):
        print(f"{self.name}, Your balance is ${self.account.balance}")
        return self


# New User
user1 = User("Mark", "bebe@gmail.com")

user1.make_deposit(200)  # balance is 200
user1.make_withdraw(50)  # balance is 150
user1.make_deposit(100)  # balance is 250
user1.display_user_balance()
