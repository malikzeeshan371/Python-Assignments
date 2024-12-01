
# 15. Write a function `sort_teams_by_size` that takes a game dictionary and returns a list of team names sorted by
# the number of players in ascending order. Example: Input: {'game_name': 'Championship', 'teams': {'TeamA': [
# 'Alice', 'Bob'], 'TeamB': ['Charlie', 'Dave', 'Eve']}} Output: ['TeamA', 'TeamB']


def sort_teams_by_size(game):
    game_sort = sorted(game['teams'])
    return game_sort
    




input_2 = {'game_name': 'Championship', 'teams': {'TeamA': ['Alice', 'Bob'], 'TeamB': ['Charlie', 'Dave','Eve']}}
print(sort_teams_by_size(input_2))