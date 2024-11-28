# 3. Write a function `remove_player` that takes a team dictionary and a player name,
# and removes the player from the team's list of players.
# Example:
# Input: team = {'DreamTeam': ['Alice', 'Bob', 'Charlie']}
#        remove_player(team, 'Bob')
# Output: {'DreamTeam': ['Alice', 'Charlie']}

def remove_player(team , player_name):
    for team_name in team:
        team[team_name].remove(player_name)

    return team

team = {'DreamTeam': ['Alice', 'Bob', 'Charlie']}
print(remove_player(team , 'Bob'))