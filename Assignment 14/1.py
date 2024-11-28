# 1. Write a function `create_team` that takes a team name and a list of player names,
# and returns a dictionary where the team name is the key and the list of players is the value.
# Example:
# Input: create_team("DreamTeam", ["Alice", "Bob", "Charlie"])
# Output: {'DreamTeam': ['Alice', 'Bob', 'Charlie']}

def create_team(team_name , player_names):
    return{
       team_name : player_names
    }

print(create_team("DreamTeam", ["Alice", "Bob", "Charlie"]))