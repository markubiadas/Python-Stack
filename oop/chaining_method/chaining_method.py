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
        print(f"{self.first_name}")
        print(f"{self.last_name}")
        print(f"{self.email}")
        print(f"{self.age}")
        print(f"{self.is_rewards_member}")
        print(f"{self.gold_card_points}")
        print("")
        return self
        
    # enroll(self) - Have this method change the user's member status to True and set their gold card points to 200.
    def enroll(self):
        self.is_rewards_member = True
        self.gold_card_points = 200
        return self
        
    # spend_points(self, amount) - have this method decrease the user's points by the amount specified.
    def spend_points(self, amount):
        self.gold_card_points = self.gold_card_points - amount
        return self
        


user1 = User("Mark", "Ubiadas", "mubiadas@gmail.com", 32)
user2 = User("Naruto", "Uzumaki", "greatesthokage@gmail.com", 21)
user3 = User("Sasuke", "Uchiha", "narutoforever@gmail.com", 21)


# Chaining method
user1.display_info().enroll().spend_points(50).display_info()
user2.enroll().spend_points(80).display_info()
user3.display_info()
