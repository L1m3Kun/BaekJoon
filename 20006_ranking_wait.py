# 20006번 랭킹 대기열
import sys
input = sys.stdin.readline
def Solution(p, m, player_list):
    Game_Rooms = {}
    level_limits = {}
    room_id = 0
    for level, nickname in player_list:
        # print("player level =", level)
        # print("player Nickname =", nickname)
        level = int(level)
        if level_limits:
            for key, val in level_limits.items():
                if val[0] <= level <= val[1]:
                    # print("플레이어 입장!", key,"번방!")
                    Game_Rooms[key] += [(level, nickname)]
                    # print("전체 방: ", Game_Rooms)
                    break
            else:
                Game_Rooms[room_id] = [(level, nickname)]
                # print("새로운 방 생성!", room_id,"번방!")
                level_limits[room_id] = [level-10, level+10]
              
                room_id += 1
                # print("전체 방 = ", Game_Rooms)
                # print("방의 레벨 제한=", level_limits)
            for key, val in Game_Rooms.items():
                if len(val) == m:
                    print("Started!")
                    val.sort(key=lambda x:x[1])
                    [print(*i) for i in val]
                    # print("만원방 삭제!", i,"번방!")
                    level_limits.pop(key)
                    Game_Rooms.pop(key)
                    break
        else:
            # print("새로운 방 생성!", room_id,"번방!")
            Game_Rooms[room_id] = [(level, nickname)]
            level_limits[room_id] = [level-10, level+10]
            room_id += 1
    for key, val in Game_Rooms.items():
        # if len(room) == m:
        #     print("Started!")
        #     # room.sort(key=lambda x:x[1])
        #     # [print(*room[i]) for i in range(m)]
        #     # print(*sorted(room, key=lambda x: x[1]), sep="\n")
        # else:
        print("Waiting!")
            # print(*sorted(Game_Rooms[room], key=lambda x: x[1]), sep="\n")
        val.sort(key=lambda x:x[1])
        [print(*i) for i in val]

p, m = map(int, input().strip().split())
player_list = [list(input().strip().split()) for _ in range(p)]

Solution(p, m, player_list)
          