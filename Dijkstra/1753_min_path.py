import sys
import heapq
input = sys.stdin.readline

#  dijkstra
def dijkstra(s, V):
    que = []
    # 최소 힙 사용 ( 가중치와 위치 데이터가 바뀌면 왜 시간이 달라지는가?)
    heapq.heappush(que, (0, s))
    Dist[s] = 0
    while que:
        t, i = heapq.heappop(que)
        if t > Dist[i]:
            continue
        for k, j in arr[i]:
            next_w = t + k
            if Dist[j] > next_w:
                heapq.heappush(que,(next_w, j))
                Dist[j] = next_w
    return




V, E = map(int, input().split())
s = int(input())
INF = 1000000
arr = [[] for _ in range(V+1)]
#  인접 데이터 초기화
for _ in range(E):
    u, v, w = map(int, input().split())
    arr[u].append((w,v))
# dp 리스트 생성
Dist = [INF] * (V+1)
dijkstra(s, V)
#  출력 맞추기
for i in range(1,V+1):
    if Dist[i] == INF:
        print("INF")
    else:
        print(Dist[i])

