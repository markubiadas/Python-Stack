players = [
    {
        "name": "Kevin Durant",
        "age": 34,
        "position": "small forward",
        "team": "Brooklyn Nets"
    },
    {
        "name": "Jason Tatum",
        "age": 24,
        "position": "small forward",
        "team": "Boston Celtics"
    },
    {
        "name": "Kyrie Irving",
        "age": 32,
        "position": "Point Guard",
        "team": "Brooklyn Nets"
    },
    {
        "name": "Damian Lillard",
        "age": 33,
        "position": "Point Guard",
        "team": "Portland Trailblazers"
    },
    {
        "name": "Joel Embiid",
        "age": 32,
        "position": "Power Foward",
        "team": "Philidelphia 76ers"
    },
    {
        "name": "DeMar DeRozan",
        "age": 32,
        "position": "Shooting Guard",
        "team": "Chicago Bulls"
    }
]

# Challenge 1: Update the Constructor
# Update the constructor to accept a dictionary with a single player's information instead of individual arguments for the attributes.


class Player:
    def __init__(self, data):
        self.name = data['name']
        self.age = data['age']
        self.position = data['position']
        self.team = data['team']

    def display_info(self):
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")
        print(f"Position: {self.position}")
        print(f"Team: {self.team}")
        print("")
        return self

    def __repr__(self):
        return f"{self.name}"


# print(players[0]['name'])
# player_1 = Player(players[0])
# print(player_1.team)

# Challenge 2: Create instances using individual player dictionaries.

kevin = {
    "name": "Kevin Durant",
    "age": 34,
    "position": "small forward",
    "team": "Brooklyn Nets"
}
jason = {
    "name": "Jason Tatum",
    "age": 24,
    "position": "small forward",
    "team": "Boston Celtics"
}
kyrie = {
    "name": "Kyrie Irving",
    "age": 32,
    "position": "Point Guard",
    "team": "Brooklyn Nets"
}


# Create your Player instances here
# Player: Kevin
player_kevin = Player(kevin)
# Player: Jason
player_jason = Player(jason)
# Player: Kyrie
player_kyrie = Player(kyrie)

# Challenge 3: Make a list of Player instances from a list of dictionaries
# Finally, given the example list of players at the top of this module (the one with many players) write a for loop that will populate an empty list with Player objects from the original list of dictionaries.

# ... (class definition and large list of players here)
new_team = []
# Write your for loop here to populate the new_team variable with Player objects.
for a_player in players:
    new_player = Player(a_player)
    new_team.append(new_player)

print(new_team)

# def see_new_team():
#     for player in new_team:
#         return player.display_info()

# see_new_team()

