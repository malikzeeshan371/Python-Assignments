

# 10. Write a function `team_with_most_players` that takes a game dictionary and returns the name of the team with
# the most players. Example: Input: {'game_name': 'Championship', 'teams': {'TeamA': ['Alice', 'Bob'],
# 'TeamB': ['Charlie', 'Dave', 'Eve']}} Output: 'TeamB'

def team_with_most_players(game):
    number_of_teams = game['teams']
    print(number_of_teams)
    # keymax = max(number_of_teams.values())
    
    # return name_of_team
    
    for most_players in number_of_teams.values():
      
        size = len(most_players)
        print(size)
    if number_of_teams['TeamA'] > number_of_teams['TeamB']:
            max_team = print('TeamA')
    else:
            max_team = print('TeamB')
  
    return max_team
        
     
    


Input_teams=  {'game_name': 'Championship', 'teams': {'TeamA': ['Alice', 'Bob'], 'TeamB': ['Charlie', 'Dave', 'Eve']}}
print(team_with_most_players(Input_teams))
