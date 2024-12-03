

# 11. Write a function `player_statistics` that takes a game dictionary and returns a dictionary where each player is
# a key, and the value is the number of teams that the player is part of. Example: Input: {'game_name':
# 'Championship', 'teams': {'TeamA': ['Alice', 'Bob'], 'TeamB': ['Bob', 'Charlie']}} Output: {'Alice': 1, 'Bob': 2,
# 'Charlie': 1}

def player_statistics(game):
    getting_players = game['teams']
    players_count = {}
    print(getting_players)
    for team_name, player_name in getting_players.items():
        for players in player_name:
            print(players)
            if players in players_count:
                players_count[players] += 1
            else:
                players_count[players] = 1
    return players_count

       
    
    
            


Input_teams1=  {'game_name': 'Championship', 'teams': {'TeamA': ['Alice', 'Bob'], 'TeamB': ['Bob','Charlie']}}
print(player_statistics(Input_teams1))