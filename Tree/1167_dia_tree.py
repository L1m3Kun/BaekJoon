import sys
from collections import deque

input = sys.stdin.readline

V = int(input())
tree = [[] for _ in range(V+1)]
for _ in range(V):
    arr = list(map(int, input().strip().split()))
    
    for i in range(1, len(arr)-1, 2):
        if (arr[0], arr[i+1]) not in tree[arr[i]]:
            tree[arr[0]].append((arr[i], arr[i+1])) 
# print(tree)
max_val = max_value = 0
for i in range(1, (V+1)//2):
    stack = deque([i])
    visited = [0] * (V+1)
    visited[i] = 1
    while stack:
        j = stack.popleft()
        for k, dis in tree[j]:
            if max_val < dis:
                spot = k
                max_val = dis
        if not visited[spot]:
            visited[spot] = visited[j] + max_val
            stack.append(spot)
    max_value = max(max_value, *visited)
            # if not visited[k]:
            #     visited[k] += visited[j] + dis
            #     stack.append(k)
                # if max_val < visited[k]:
                #     max_val=visited[k]
print(max_value-1)       
