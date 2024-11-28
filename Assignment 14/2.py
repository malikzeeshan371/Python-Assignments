
# 2. Write a function `add_player` that takes a team dictionary, a player name, and adds the player to the team's
# list of players. Example: Input: team = {'DreamTeam': ['Alice', 'Bob']} add_player(team, 'Charlie') Output: {
# 'DreamTeam': ['Alice', 'Bob', 'Charlie']}

def add_player(team,player_name):
    for team_name in team:
        team[team_name].append(player_name)
    return team

  
    
       
    

team = {'DreamTeam': ['Alice', 'Bob']}
print(add_player(team , 'Charlie'))
