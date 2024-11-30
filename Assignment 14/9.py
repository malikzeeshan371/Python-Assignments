

# 9. Write a function `average_team_size` that takes a game dictionary and returns the average size of the teams.
# Example:
# Input: {'game_name': 'Championship', 'teams': {'TeamA': ['Alice', 'Bob'], 'TeamB': ['Charlie', 'Dave', 'Eve']}}
# Output: 2.5

def average_team_size(game):
    
    number_of_players = game['teams']
    number_of_teams = len(number_of_players)
    
    for numbers in number_of_players:
        total_numbers = len(numbers)
        avg = total_numbers/number_of_teams
    return avg

     


Input_teams=  {'game_name': 'Championship', 'teams': {'TeamA': ['Alice', 'Bob'], 'TeamB': ['Charlie', 'Dave', 'Eve']}}
print(average_team_size(Input_teams))