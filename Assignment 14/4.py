# 4. Write a function `team_summary` that takes a team dictionary and returns a summary string
# showing the team name and the number of players.
# Example:
# Input: {'DreamTeam': ['Alice', 'Charlie']}
# Output: 'Team DreamTeam has 2 players.'



def team_summary(team):
    for  value in team.values():
        sum = len(value)
    return sum


team_new = {'DreamTeam': ['Alice', 'Charlie']}
print("Team dream has" , team_summary(team_new) , "players")