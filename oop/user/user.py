class User:
    def __init__(self, first_name, last_name, email, age):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.age = age
        self.is_rewards_member = False
        self.gold_card_points = 0
    
    # display_info(self) - Have this method print all of the users' details on separate lines. 
    def display_info(self):
        print(f"Name: {self.first_name} {self.last_name}")
        print(f"Email: {self.email}")
        print(f"Age: {self.age}")
        print(f"Rewards Member: {self.is_rewards_member}")
        print(f"Gold Points: {self.gold_card_points}")
        print("")
        
    # enroll(self) - Have this method change the user's member status to True and set their gold card points to 200.
    def enroll(self):
        self.is_rewards_member = True
        self.gold_card_points = 200
        
    # spend_points(self, amount) - have this method decrease the user's points by the amount specified.
    def spend_points(self, amount):
        self.gold_card_points = self.gold_card_points - amount
        

# In the outer scope, create a user instance and call the display_info method to test.
user1 = User("Mark", "Ubiadas", "mubiadas@gmail.com", 32)
user1.display_info()
# Enroll method implemented and test by calling the method on the user in the outer scope.
user1.enroll()
user1.display_info()

# Make 2 more instances of the User class.
user2 = User("Naruto", "Uzumaki", "greatesthokage@gmail.com", 21)
user3 = User("Sasuke", "Uchiha", "narutoforever@gmail.com", 21)

# Have the first user spend 50 points
user1.spend_points(50)

# Have the second user enroll.
user2.enroll()

# Have the second user spend 80 points
user2.spend_points(80)

user1.display_info()
user2.display_info()
user3.display_info()

