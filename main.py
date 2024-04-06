import random
from itertools import combinations

class TableTenins:
    def __init__(self,rounds,players):
        self.rounds = rounds
        self.players = players
        self.shuffled_combinations = list(combinations(range(1,players+1),2))
        # random.shuffle(self.shuffled_combinations)
        self.points = []

    def distribute_players(self):
        paired_players = []
        while len(paired_players) != self.players:
            for i in self.shuffled_combinations:
                s = i
                if (not s[0] in paired_players) and (not s[1] in paired_players):
                    paired_players.append(s[0])
                    paired_players.append(s[1])
                    self.shuffled_combinations.remove(s)
        return paired_players

    # You will already get a list of teams. I think it's already on self class. You must decide which teams plays against whom.
    def distribute_teams(self):
        pass

    # Must still remove the players
    # And also add that the player already played with another player
    # So a function like set_pairs must be added, which changes the players_already_played_with list

    def main(self):
        if self.players % 4 == 0:
            for i in range(self.rounds):
                print(self.distribute_players())


if __name__ == "__main__":
    print("Starting")
    t = TableTenins(6,16)
    t.main()