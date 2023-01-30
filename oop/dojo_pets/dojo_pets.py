# ====================== Ninja Class ====================

class Ninja:
    # implement __init__( first_name , last_name , treats , pet_food , pet )
    def __init__(self, first_name, last_name, treats, pet_food, pet):
        self.first_name = first_name
        self.last_name = last_name
        self.treats = treats
        self.pet_food = pet_food
        self.pet = pet

# ==================== Ninja Methods =========================

    # implement the following methods:
    
    # walk() - walks the ninja's pet invoking the pet play() method
    def walk(self):
        self.pet.play()
        print(f"{self.first_name} is walking {self.pet.name}.")
        
        if self.pet.health < 100:
            print(f"{self.pet.name}'s health increases by 5 and is now {self.pet.health}!")
        else:
            print(f"{self.pet.name} reached the max health: 100.")
        print("")

        return self

    # feed() - feeds the ninja's pet invoking the pet eat() method
    def feed(self):
        self.pet.eat()

        print(f"{self.first_name} is feeding {self.pet.name} with {self.treats}!")
        if self.pet.energy < 100:
            print(
                f"{self.pet.name}'s energy increases by 5 and is now {self.pet.energy}.")
        else:
            print(f"{self.pet.name} reached the max energy: 100.")


        if self.pet.health < 100:
            print(
                f"{self.pet.name}'s health increases by 10 and is now {self.pet.health}.")
        else:
            print(f"{self.pet.name} reached the max health: 100.")
        print("")

        return self

    # bathe() - cleans the ninja's pet invoking the pet noise() method
    def bathe(self):
        self.pet.noise()
        print(f"{self.first_name} is cleaning {self.pet.name}!")
        print("")
        return self

# =================== Pet Class =======================

class Pet:
    def __init__(self, name, type, tricks):
        self.name = name
        self.type = type
        self.tricks = tricks
        self.health = 75
        self.energy = 70

# ================ Pet Methods =====================

    def sleep(self):
        self.energy += 25
        return self

    def eat(self):
        # ===== Energy =====
        if self.energy < 100:
            self.energy += 5
        else:
            self.energy = 100
        # ====== Health ======
        if self.health < 100:
            self.health += 10
        else:
            self.health = 100

        return self

    def play(self):
        if self.health < 100:
            self.health += 5
        else:
            self.health = 100

        return self

    def noise(self):
        print(f"{self.name} is singing.")
        return self

# =================================================================

mochi = Pet("Mochi", "Chihuahua", "Shake-hands")
mark = Ninja("Mark", "Ubiadas", "ice cream", "fries", mochi)

mark.feed()
mark.walk()
mark.bathe()
