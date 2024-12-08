

# 10. Write a function `team_with_most_players` that takes a game dictionary and returns the name of the team with
# the most players. Example: Input: {'game_name': 'Championship', 'teams': {'TeamA': ['Alice', 'Bob'],
# 'TeamB': ['Charlie', 'Dave', 'Eve']}} Output: 'TeamB'

def team_with_most_players(game):
    number_of_teams = game['teams']
    # print(number_of_teams)
    # keymax = max(number_of_teams.values())
    
    # return name_of_team
    max_team = ''
    max_count = 0
    for teams, team_players in number_of_teams.items():
      if len(team_players) >max_count:
         max_team = teams
         max_count = len(team_players)
    return max_team
    


Input_teams=  {'game_name': 'Championship', 'teams': {'TeamA': ['Alice', 'Bob'], 'TeamB': ['Charlie', 'Dave', 'Eve']}}
print(team_with_most_players(Input_teams))
