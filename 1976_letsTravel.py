# 1976 여행가자
import sys
from collections import deque
input = sys.stdin.readline

N = int(input())
M = int(input())

linked = [ [] for _ in range(N+1)]
# print(linked)
for country in range(1,N+1):
    route = list(map(int, input().split()))
    for b in range(N):
        if route[b]:
            linked[country].append(b+1)
travel = deque(map(int,input().split()))
# print(linked)

check = set()
# for i in linked:
#     for j in range(M):
#         if travel[j] in linked[i]:
#             check.add(travel[j])
# print(check)
check.add(travel[0])
for spot in travel:
    for i in range(M):
        if travel[i] in linked[spot]:
            check.add(travel[i])
# print(check)
print("YES") if len(check) == M else print("NO")

# 1976 여행가자
import sys
input = sys.stdin.readline

N = int(input())
M = int(input())

linked = [ [] for _ in range(N+1)]
# print(linked)
for country in range(1,N+1):
    route = list(map(int, input().split()))
    for b in range(N):
        if route[b]:
            linked[country].append(b+1)
travel = list(map(int,input().split()))

check = set()
for i in range(1,N+1):
    for j in range(M):
        if travel[j] in linked[i]:
            check.add(j)

print("YES") if len(check) == M else print("NO")