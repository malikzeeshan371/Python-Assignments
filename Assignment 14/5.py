

# 5. Write a function `create_game` that takes a game name and a dictionary of teams (each represented by a list of
# players), and returns a dictionary representing the game with the game name and teams. Example: Input: teams = {
# 'TeamA': ['Alice', 'Bob'], 'TeamB': ['Charlie', 'Dave']} create_game('Championship', teams) Output: {'game_name':
# 'Championship', 'teams': {'TeamA': ['Alice', 'Bob'], 'TeamB': ['Charlie', 'Dave']}}

def create_game(game_name , teams):
    return{
        'game_name': game_name,
        'Teams' : teams
    }

Teams_input = {'TeamA': ['Alice', 'Bob'], 'TeamB': ['Charlie', 'Dave']}
print(create_game('Championship', Teams_input))