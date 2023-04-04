import sys
from itertools import combinations
input = sys.stdin.readline

N, M, D = map(int, input().strip().split())
field = [list(map(int, input().strip().split())) for _ in range(N)]

def distance(r1, c1, r2, c2):
    return abs(r1-r2) + abs(c1-c2)

def find_enermy(n):
    global tmp
    enermy = 0
    for i in range(N-1, n-1, -1):
        for j in range(M):
            if tmp[i][j] >= 1:
                enermy += 1
    return enermy  

def kill_enermy(stage, place):
    global tmp
    target = []
    for i in range(D//2):
        for j in range(-abs(D//2-i), abs(D//2-i)+1):
            if 0<= stage-i< N and 0<= place+j < M:
                if tmp[stage-i][place+j] == 1:
                    target.append((stage-i, place+j))
    if target:
        target.sort(key=lambda x:x[2])
        return (target[0][0],target[0][1])
    return 0

def kill(stage, place):
    global tmp
    enermy = set()
    cnt = 0
    for i in range(3):
        a = kill_enermy(stage, place[i]) 
        if a != 0:
            enermy.add(a)
    for i, j in enermy:
        tmp[i][j] = 0
        cnt += 1
    return cnt
    

def clear_death(n):
    global tmp
    for i in range(N-1, n, -1):
        for j in range(M):
            if tmp[i][j] > 1:
                tmp[i][j] = 0
    return

def game_start():
    global tmp
    arr = [i for i in range(M)]
    place = combinations(arr, 3)
    maxV = 0
    for archer in place:
        killed = 0
        for j in range(N):
            for k in range(M):
                tmp[j][k] = field[j][k]
        for i in range(N-1, -1, -1):
            if find_enermy(i):
                killed += kill(i, archer)
                clear_death(i)
    
    maxV = max(killed, maxV)
    return maxV

tmp = [[0] * M for _ in range(N)]
print(game_start())




# import sys
# input = sys.stdin.readline

# # def distance(r1, c1, r2, c2):
# #     return abs(r1-r2) + abs(c1-c2)

# # def game_start(i, cnt, val):
# #     global max_kda
    
# #     if i == M:
# #         return
# #     if cnt == 3:
# #         max_kda = max(max_kda, val)
# #         return

# #     tmp = [[0] *M for _ in range(N)]
# #     for k in range(N):
# #         tmp[k] = field[k].copy()
# #     game_start(i+1, cnt + 1, val + score(i))
# #     for k in range(N):
# #         field[k] = tmp[k].copy()
# #     game_start(i+1, cnt, val)
# #     return

# def game(stack):
#     global max_kda
#     if len(stack) == 3:
#         tmp = [[0] * M for _ in range(N)]
#         for k in range(N):
#             tmp[k] = field[k].copy()
#         max_kda = max(score1(stack), max_kda)
#         for k in range(N):
#             field[k] = tmp[k].copy()
#         return
#     for i in range(M):
#         if i not in stack:
#             stack.append(i)
#             game(stack)
#             stack.pop()



# def score1(place):
#     kda = 0
#     # arr = [[0]*N for _ in range(M)]
#     # for i in range(N):
#     #     for j in range(M):
#     #         arr[i][j] = field[i][j]
#     for i in range(N-1, -1, -1):
#         for idx in range(3):
#             kda += one_archer_kill(i, place[idx])
#         for j in range(i):
#             for k in range(M):
#                 if field[j][k] >1:
#                     field[j][k] = 0
#     return kda
# def score(place):
#     kda = 0
#     # arr = [[0]*N for _ in range(M)]
#     # for i in range(N):
#     #     for j in range(M):
#     #         arr[i][j] = field[i][j]
#     for i in range(N-1, -1, -1):
#         kda += one_archer_kill(i, place)
#         for j in range(i):
#             for k in range(M):
#                 if field[j][k] >1:
#                     field[j][k] = 0
#     return kda


# def one_archer_kill(stage, place):
#     res = []
#     for i in range(D):
#         for j in range(-abs(D//2-i), abs(D//2-i)+1):
#             if 0<=stage-i<N and 0<=place+j<M and field[stage-i][place+j] >= 1:
#                 # field[stage-i][place+j] = 2
#                 # return 1
#                 res.append((stage-i, place+j,abs(i)+abs(j)))
#     if res:
#         res.sort(key=lambda x:x[2])
#         # if field[res[0][0]][res[0][1]] == 1:
#         #     field[res[0][0]][res[0][1]] = 2
#         #     return 1
#         for i in range(len(res)):
#             if field[res[i][0]][res[i][1]] == 1:
#                 field[res[i][0]][res[i][1]] = 2
#                 return 1

#     return 0

# N, M, D = map(int, input().strip().split())
# field = [list(map(int, input().strip().split())) for _ in range(N)]
# max_kda = 0
# # game_start(0, 0, 0)
# game([])
# print(max_kda)





# import sys
# input = sys.stdin.readline

# def distance(r1, c1, r2, c2):
#     return abs(r1-r2) + abs(c1-c2)

# # def game_start1(i, cnt, val):
# #     global max_kda
    
# #     if cnt == 3:
# #         max_kda = max(max_kda, val)
# #         return
# #     if i == M:
# #         return

# #     tmp = [[0] *M for _ in range(N)]
# #     for k in range(N):
# #         tmp[k] = field[k].copy()
# #     game_start(i+1, cnt + 1, val + score(i))
# #     for k in range(N):
# #         field[k] = tmp[k].copy()
# #     game_start(i+1, cnt, val)
# #     return


# def set_archer(arr):
#     global maxV
#     if len(arr) == 3:
#         # tmp = [[0] * M for _ in range(N)]
#         # for i in range(N):
#         #     for j in range(M):
#         #         tmp[i][j] = field[i][j]
#         score = game_start(arr)
#         maxV = max(maxV, score)
#         return
#     for i in range(M):  
#         if i not in arr:
#             arr.append(i)
#             set_archer(arr)
#             arr.pop()


# def game_start(place):
#     cnt = 0
#     tmp = [[0] * M for _ in range(N)]
#     for i in range(N):
#         for j in range(M):
#             tmp[i][j] = field[i][j]
#     for i in range(N-1, -1, -1):
#         for j in range(3):
#             # score += kill_enermy(i,place[j], tmp)
#             score = []
#             for k in range(D):
#                 for l in range(-abs(D//2-k), abs(D//2-k)+1):
#                     if 0<=i-k<N and 0<=place[j]+l<M and tmp[i-k][place[j]+l]>=1:
#                         score.append((i-k, place[j]+l, distance(i,place[j], i-k, j+l)))
#             if score:
#                 score.sort(key=lambda x: x[2])
#                 # print(score)
#                 # for t in range(len(score)):
#                 #     if tmp[score[t][0]][score[t][1]] == 1:
#                 #         tmp[score[t][0]][score[t][1]] = 2
#                 #         cnt += 1
#                 #         break
#                 if tmp[score[0][0]][score[0][1]] == 1:
#                     tmp[score[0][0]][score[0][1]] = 2
#                     cnt += 1
#         for j in range(i):
#             for k in range(M):
#                 if field[j][k] > 1:
#                     field[j][k]=0
#     return cnt


# def kill_enermy(stage, place, arr):
#     score = []
#     for i in range(D):
#         for j in range(-abs(D//2-i), abs(D//2-i)+1):
#             if 0<=stage-i<N and 0<=place+j<M and arr[stage-i][place+j]:
#                 score.append((stage-i, place+j, distance(stage, place, stage-i, place+j)))
#     if score:
#         score.sort(key=lambda x: x[2])
#         # print(score)
#         if arr[score[0][0]][score[0][1]] == 1:
#             arr[score[0][0]][score[0][1]] = 2
#             return 1
        
#         # for i in range(len(score)):
#         #     if arr[score[i][0]][score[i][1]] == 1:
#         #         return 1
#     return 0

# N, M, D = map(int, input().split())
# field = [list(map(int, input().split())) for _ in range(N)]
# maxV = 0
# stack = []
# set_archer(stack)
# print(maxV)

        
