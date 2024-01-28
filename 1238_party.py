# 1238 파티
import sys, heapq
input = sys.stdin.readline


def dijkstra(start:int, target:int, graph:list, N:int) -> int:
    que = []
    heapq.heappush(que, (0, start))

    while que:
        cost, now = heapq.heappop(que)
        if now == target:
            return cost
        for i in range(1, N+1):
            if graph[now][i] > 0:
                heapq.heappush(que, (cost+graph[now][i], i))


def solution():
    N, M, X = map(int, input().split())
    graph = [[0] * (N+1) for _ in range(N+1)]
    for _ in range(M):
        s, e, c = map(int, input().split())
        graph[s][e] = c
    members = [0] * (N+1)
    for i in range(1, N+1):
        if i == X:
            continue
        members[i] += dijkstra(i, X, graph, N)
    members[i] += dijkstra(X, i, graph, N)
    print(max(members[1:]))
    # print(members)

if __name__ == "__main__":
    solution()