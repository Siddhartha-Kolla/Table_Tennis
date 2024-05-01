import random
from itertools import combinations

class TableTenins:
    def __init__(self,rounds,players):
        self.rounds = rounds
        self.players = players
        self.shuffled_combinations = list(combinations(range(1,players+1),2))
        # print(len(self.shuffled_combinations))
        # random.shuffle(self.shuffled_combinations)
        self.points = []

    def distribute_players(self):
        rounds = []
        players_list = [i for i in range(1,self.players+1)]
        for i in range(1,self.players):
            game = []
            for x in range(1,(self.players//2)+1):
                game.append((players_list[x-1],players_list[x*(-1)]))
            turned_list = players_list[1:]
            turned_list_final = [players_list[0]]
            turned_list_final.extend(turned_list[-1:] + turned_list[:-1])
            players_list = turned_list_final
            rounds.append(game)
        return rounds

    # You will already get a list of teams. I think it's already on self class. You must decide which teams plays against whom.
    def distribute_teams(self):
        pass

    # Must still remove the players
    # And also add that the player already played with another player
    # So a function like set_pairs must be added, which changes the players_already_played_with list

    def main(self):
        if self.players % 4 == 0:
            # print(self.shuffled_combinations)
            c = self.distribute_players()
            print(len(c))
            for i in c:
                print(i)



if __name__ == "__main__":
    print("Starting")
    players = 20
    max_rounds = int((len(list(combinations(range(1,players+1),2))))//(players//2))
    t = TableTenins(max_rounds,players)
    t.main()