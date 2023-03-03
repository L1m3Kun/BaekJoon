import sys

input = sys.stdin.readline


N, M, V = map(int, input().strip().split())
# 무향 그래프 만들기
graph = [[] for _ in range(N+1)]
for _ in range(M):
    spot, node = map(int, input().strip().split())
    graph[spot].append(node)
    graph[node].append(spot)

stack = [V]
queue = [V]
dfs_visited = [0] * (N+1)
bfs_visited = [0] * (N+1)
dfs_visited[V] = 1
res = []            # 결과 출력용
# DFS
while stack:
    dfs = stack.pop()
    dfs_visited[dfs] = 1
    if dfs not in res:
        res.append(dfs)     # 경로에 가본적 없으면 저장
    graph[dfs].sort(reverse=1)
    for i in graph[dfs]:
        if not dfs_visited[i]:
            stack.append(i)
print(*res)
# BFS
bfs_visited[V] = 1
while queue:
    bfs = queue.pop(0)
    print(bfs, end=' ')
    graph[bfs].sort()
    for i in graph[bfs]:
        if not bfs_visited[i]:
            bfs_visited[i] = 1
            queue.append(i)
print()
