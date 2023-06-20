# 25757 임스와 함께하는 미니게임
import sys
input = sys.stdin.readline

player_limit={
    'Y': 1,
    'F': 2,
    'O': 3,
}

N, GameType = input().strip().split()
N = int(N)
players= [input().strip() for _ in range(N)]
played_players = set()
game_room = set()
limit = player_limit[GameType]
game_count = 0
count = 1
for player in players:
    count += 1
    if not player in played_players:
        played_players.add(player)
        game_room.add(player)
    if len(game_room) == limit:
        game_count += 1
        game_room.clear()
print(game_count)
        

#########
''' ㅋ 이게더 쉽고 빠름
import sys
input = sys.stdin.readline
N, GameType = input().strip().split()
players= {input().strip() for _ in range(int(N))}
player_num = len(players)
print(player_num if GameType == 'Y' else player_num//2 if GameType == 'F' else player_num//3)
'''