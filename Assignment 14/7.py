
# 7. Write a function `remove_team_from_game` that takes a game dictionary and a team name,
# and removes the team from the game.
# Example:
# Input: game = {'game_name': 'Championship', 'teams': {'TeamA': ['Alice', 'Bob'], 'TeamB': ['Charlie', 'Dave']}}
#        remove_team_from_game(game, 'TeamB')
# Output: {'game_name': 'Championship', 'teams': {'TeamA': ['Alice', 'Bob']}}

def remove_team_from_game(game , team_name):
    team_namee = game['teams']
    
    
    del team_namee[team_name]
    return game
    
        
    

game_1 = {'game_name': 'Championship', 'teams': {'TeamA': ['Alice', 'Bob'], 'TeamB': ['Charlie', 'Dave']}}
print(remove_team_from_game(game_1,'TeamB'))

