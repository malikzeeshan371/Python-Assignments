
# 8. Write a function `game_summary` that takes a game dictionary and returns a summary string
# showing the game name and the number of teams.
# Example:
# Input: {'game_name': 'Championship', 'teams': {'TeamA': ['Alice', 'Bob']}}
# Output: 'Game Championship has 1 team.'

def game_summary(game):
    game_name = game['game_name']
    number_of_teams = len(game['teams'])
    return f"Game{game_name} has {number_of_teams} team"
input_1 = {'game_name': 'Championship', 'teams': {'TeamA': ['Alice', 'Bob']}}
print(game_summary(input_1))