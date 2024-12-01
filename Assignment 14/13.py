
# 13. Write a function `update_player_list` that takes a game dictionary, a team name, and a new list of players,
# and updates the team's player list with the new list.
# Example:
# Input: game = {'game_name': 'Championship', 'teams': {'TeamA': ['Alice', 'Bob']}}
#        update_player_list(game, 'TeamA', ['Alice', 'Bob', 'Charlie'])
# Output: {'game_name': 'Championship', 'teams': {'TeamA': ['Alice', 'Bob', 'Charlie']}}

def update_player_list(game,team_name,players):
    list_of_players = game['teams']
    list_of_players.update({team_name : players})
    return game    
game_1 = {'game_name': 'Championship', 'teams': {'TeamA': ['Alice', 'Bob']}}

print(update_player_list(game_1, 'TeamA', ['Alice', 'Bob', 'Charlie']))
