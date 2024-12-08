

# 6. Write a function `add_team_to_game` that takes a game dictionary and a team name with a list of players,
# and adds the team to the game.
# Example:
# Input: game = {'game_name': 'Championship', 'teams': {'TeamA': ['Alice', 'Bob']}}
#        game = {'game_name': 'Championship', 'teams': {'TeamA': ['Alice', 'Bob']}}
# Output: {'game_name': 'Championship', 'teams': {'TeamA': ['Alice', 'Bob'], 'TeamB': ['Charlie', 'Dave']}}

def add_team_to_game(game , team):
    game['teams'].update(team)
    return game

game= {'game_name': 'Championship', 'teams': {'TeamA': ['Alice', 'Bob']}}
# game= {'game_name': 'Championship', 'teams': {'TeamB': ['Alice', 'Bob']}}


print(add_team_to_game(game,{'TeamB':['Charlie', 'Dave']}))
