import random
from itertools import combinations

class TableTenins:
    def __init__(self,rounds,players):
        self.rounds = rounds
        self.players = players
        self.shuffled_combinations = list(combinations(range(1,players+1),2))
        print(len(self.shuffled_combinations))
        # random.shuffle(self.shuffled_combinations)
        self.points = []

    def distribute_players(self):
        paired_players = []
        while len(paired_players) != int(self.players//2):
            turned_list = self.shuffled_combinations[int(len(self.shuffled_combinations)//2) :] + self.shuffled_combinations[:int(len(self.shuffled_combinations)//2)]
            for i in turned_list:
                if (not i[0] in set(elem for tpl in paired_players for elem in tpl)) and (not i[1] in set(elem for tpl in paired_players for elem in tpl)):
                    paired_players.append(i)
                    self.shuffled_combinations.remove(i)
                    break
        return paired_players

    # You will already get a list of teams. I think it's already on self class. You must decide which teams plays against whom.
    def distribute_teams(self):
        pass

    # Must still remove the players
    # And also add that the player already played with another player
    # So a function like set_pairs must be added, which changes the players_already_played_with list

    def main(self):
        if self.players % 4 == 0:
            print(self.shuffled_combinations)
            for i in range(self.rounds):
                print(f"Round {i+1}")
                print(len(self.shuffled_combinations))
                print(self.distribute_players())


if __name__ == "__main__":
    print("Starting")
    players = 12
    max_rounds = int((len(list(combinations(range(1,players+1),2))))//(players//2))
    t = TableTenins(max_rounds,players)
    t.main()