from itertools import combinations

def distribute_pairs(combinations, num_players):
    rounds = []
    assigned_players = set()

    for pair in combinations:
        # Check if any player in the pair is already assigned to a pair in the existing rounds
        if not any(player in assigned_players for player in pair):
            # Add the pair to the current round
            rounds.append(pair)
            # Mark both players in the pair as assigned
            assigned_players.update(pair)

            # If all players are assigned, start a new round
            if len(assigned_players) == num_players:
                assigned_players = set()
                yield rounds  # Yield the current round
                rounds = []  # Start a new round

def max_rounds_possible(combinations, num_players):
    max_rounds = 0
    remaining_combinations = combinations.copy()

    while remaining_combinations:
        # Distribute pairs for one round
        for round_num, round_combinations in enumerate(distribute_pairs(remaining_combinations, num_players), 1):
            print(f"Round {round_num}: {round_combinations}")
            max_rounds += 1

        # Remove distributed pairs from the list of combinations
        for pair in round_combinations:
            remaining_combinations.remove(pair)

    return max_rounds

# Example usage
lcombinations = list(combinations(range(1,40+1),2))
print(lcombinations)
print()
num_players = 40
max_rounds = max_rounds_possible(lcombinations, num_players)
print("Maximum rounds possible:", max_rounds)
