# Assignment: Lists, Dictionaries, Nested Lists and Dictionaries, and Functions

# 1. Write a function `create_team` that takes a team name and a list of player names,
# and returns a dictionary where the team name is the key and the list of players is the value.
# Example:
# Input: create_team("DreamTeam", ["Alice", "Bob", "Charlie"])
# Output: {'DreamTeam': ['Alice', 'Bob', 'Charlie']}

# 2. Write a function `add_player` that takes a team dictionary, a player name, and adds the player to the team's
# list of players. Example: Input: team = {'DreamTeam': ['Alice', 'Bob']} add_player(team, 'Charlie') Output: {
# 'DreamTeam': ['Alice', 'Bob', 'Charlie']}

# 3. Write a function `remove_player` that takes a team dictionary and a player name,
# and removes the player from the team's list of players.
# Example:
# Input: team = {'DreamTeam': ['Alice', 'Bob', 'Charlie']}
#        remove_player(team, 'Bob')
# Output: {'DreamTeam': ['Alice', 'Charlie']}

# 4. Write a function `team_summary` that takes a team dictionary and returns a summary string
# showing the team name and the number of players.
# Example:
# Input: {'DreamTeam': ['Alice', 'Charlie']}
# Output: 'Team DreamTeam has 2 players.'

# 5. Write a function `create_game` that takes a game name and a dictionary of teams (each represented by a list of
# players), and returns a dictionary representing the game with the game name and teams. Example: Input: teams = {
# 'TeamA': ['Alice', 'Bob'], 'TeamB': ['Charlie', 'Dave']} create_game('Championship', teams) Output: {'game_name':
# 'Championship', 'teams': {'TeamA': ['Alice', 'Bob'], 'TeamB': ['Charlie', 'Dave']}}

# 6. Write a function `add_team_to_game` that takes a game dictionary and a team name with a list of players,
# and adds the team to the game.
# Example:
# Input: game = {'game_name': 'Championship', 'teams': {'TeamA': ['Alice', 'Bob']}}
#        add_team_to_game(game, 'TeamB', ['Charlie', 'Dave'])
# Output: {'game_name': 'Championship', 'teams': {'TeamA': ['Alice', 'Bob'], 'TeamB': ['Charlie', 'Dave']}}

# 7. Write a function `remove_team_from_game` that takes a game dictionary and a team name,
# and removes the team from the game.
# Example:
# Input: game = {'game_name': 'Championship', 'teams': {'TeamA': ['Alice', 'Bob'], 'TeamB': ['Charlie', 'Dave']}}
#        remove_team_from_game(game, 'TeamB')
# Output: {'game_name': 'Championship', 'teams': {'TeamA': ['Alice', 'Bob']}}

# 8. Write a function `game_summary` that takes a game dictionary and returns a summary string
# showing the game name and the number of teams.
# Example:
# Input: {'game_name': 'Championship', 'teams': {'TeamA': ['Alice', 'Bob']}}
# Output: 'Game Championship has 1 team.'

# 9. Write a function `average_team_size` that takes a game dictionary and returns the average size of the teams.
# Example:
# Input: {'game_name': 'Championship', 'teams': {'TeamA': ['Alice', 'Bob'], 'TeamB': ['Charlie', 'Dave', 'Eve']}}
# Output: 2.5

# 10. Write a function `team_with_most_players` that takes a game dictionary and returns the name of the team with
# the most players. Example: Input: {'game_name': 'Championship', 'teams': {'TeamA': ['Alice', 'Bob'],
# 'TeamB': ['Charlie', 'Dave', 'Eve']}} Output: 'TeamB'

# 11. Write a function `player_statistics` that takes a game dictionary and returns a dictionary where each player is
# a key, and the value is the number of teams that the player is part of. Example: Input: {'game_name':
# 'Championship', 'teams': {'TeamA': ['Alice', 'Bob'], 'TeamB': ['Bob', 'Charlie']}} Output: {'Alice': 1, 'Bob': 2,
# 'Charlie': 1}

# 12. Write a function `team_stats` that takes a game dictionary and returns a dictionary where each team is a key,
# and the value is the number of players in that team.
# Example:
# Input: {'game_name': 'Championship', 'teams': {'TeamA': ['Alice', 'Bob'], 'TeamB': ['Charlie', 'Dave']}}
# Output: {'TeamA': 2, 'TeamB': 2}

# 13. Write a function `update_player_list` that takes a game dictionary, a team name, and a new list of players,
# and updates the team's player list with the new list.
# Example:
# Input: game = {'game_name': 'Championship', 'teams': {'TeamA': ['Alice', 'Bob']}}
#        update_player_list(game, 'TeamA', ['Alice', 'Bob', 'Charlie'])
# Output: {'game_name': 'Championship', 'teams': {'TeamA': ['Alice', 'Bob', 'Charlie']}}

# 14. Write a function `find_team` that takes a game dictionary and a player name,
# and returns the name of the team that the player is part of, or 'Not found' if the player is not in any team.
# Example:
# Input: {'game_name': 'Championship', 'teams': {'TeamA': ['Alice', 'Bob'], 'TeamB': ['Charlie', 'Dave']}}
#        find_team(game, 'Charlie')
# Output: 'TeamB'

# 15. Write a function `sort_teams_by_size` that takes a game dictionary and returns a list of team names sorted by
# the number of players in ascending order. Example: Input: {'game_name': 'Championship', 'teams': {'TeamA': [
# 'Alice', 'Bob'], 'TeamB': ['Charlie', 'Dave', 'Eve']}} Output: ['TeamA', 'TeamB']
