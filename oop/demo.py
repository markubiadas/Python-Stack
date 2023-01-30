class BankAccount:
    def __init__(self, int_rate, balance):
        self.int_rate = int_rate
        self.balance = balance


class User:
    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.account = BankAccount(int_rate=0.02, balance=0)  # added this line

    # def example_method(self):
    #     # we can call the BankAccount instance's methods
    #     self.account.deposit(100)
    #     # or access its attributes
    #     print(self.account.balance)


user1 = User("Mark", "bebe@gmail.com")
print(user1.account.int_rate) #use dot notation to access attributes inside the class
