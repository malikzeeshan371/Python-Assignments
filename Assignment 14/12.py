
# 12. Write a function `team_stats` that takes a game dictionary and returns a dictionary where each team is a key,
# and the value is the number of players in that team.
# Example:
# Input: {'game_name': 'Championship', 'teams': {'TeamA': ['Alice', 'Bob'], 'TeamB': ['Charlie', 'Dave']}}
# Output: {'TeamA': 2, 'TeamB': 2}

def team_stats(game):
    no_of_teams = game['teams']
    for teams in no_of_teams.values():
        getting_members = len(teams)
        return{
            'TeamA': getting_members,
            'TeamB': getting_members

        }
    

Input_teams=  {'game_name': 'Championship', 'teams': {'TeamA': ['Alice', 'Bob'], 'TeamB': ['Charlie', 'Dave']}}
print(team_stats(Input_teams))