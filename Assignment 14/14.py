

# 14. Write a function `find_team` that takes a game dictionary and a player name,
# and returns the name of the team that the player is part of, or 'Not found' if the player is not in any team.
# Example:
# Input: {'game_name': 'Championship', 'teams': {'TeamA': ['Alice', 'Bob'], 'TeamB': ['Charlie', 'Dave']}}
#        find_team(game, 'Charlie')
# Output: 'TeamB'

def find_team(game , player_name):
    # game =  {'game_name': 'Championship', 'teams': {'TeamA': ['Alice', 'Bob'], 'TeamB': ['Charlie', 'Dave']}}
    
    list_of_teams = game['teams']
    #list_of_teams = {'TeamA': ['Alice', 'Bob'], 'TeamB': ['Charlie', 'Dave']}
    [('TeamA', ['Alice', 'Bob']),('TeamB', ['Charlie', 'Dave'])]
    print(list_of_teams)
    for team_nam,team_values in list_of_teams.items():
        for team_player_name in team_values:
            if team_player_name == player_name:
                return team_nam
    return 'not found'
        

input_2 = {'game_name': 'Championship', 'teams': {'TeamA': ['Alice', 'Bob'], 'TeamB': ['Charlie', 'Dave']}}
print(find_team(input_2 , 'Alice'))