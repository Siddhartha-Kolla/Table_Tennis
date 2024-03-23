import random

class TableTenins:
    def __init__(self,rounds,players):
        self.rounds = rounds
        self.players = players
        self.players_already_played_with = [[] for i in range(players)]
        self.points = []

    def distribute_players(self):
        temp_list = [i for i in range(1,self.players+1)]
        pairs = []
        while len(temp_list) != 0:
            player_1 , player_2 = random.choice(temp_list) , random.choice(temp_list)
            while player_2 == player_1 or player_2 in self.players_already_played_with[temp_list.index(player_1)-1]:
                player_2 = random.choice(temp_list)
            pairs.append([player_1,player_2])

    # You will already get a list of teams. I think it's already on self class. You must decide which teams plays against whom.
    def distribute_teams(self):
        pass

    # Must still remove the players
    # And also add that the player already played with another player
    # So a function like set_pairs must be added, which changes the players_already_played_with list

    def main(self):
        if self.players % 4 == 0:
            for i in range(self.rounds):
                self.distribute_players()