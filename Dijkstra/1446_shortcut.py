# 1446 지름길
import sys
from collections import deque
input = sys.stdin.readline

def dijkstra(s, V):

    que = deque([(0,0)])
    Dist[0] = 0
    while que:
        # 고속도로 주행
        i, k = que.popleft()
        # 갈림길 모두 가져오기
        for j,w  in arr[i]:
            # 지름길로 가는 경우에만 추가
            if 0<j<V+1 and Dist[j] > Dist[i]+w:
                que.append((j, w))
                Dist[j] = Dist[i]+w
    return 



N, D = map(int, input().split())
INF = 100000000
arr = [[(_+1, 1)] for _ in range(D+1)]
for _ in range(N):
    s, e, w = map(int, input().split())
    if not e > D and (e-s) > w:
        arr[s].append((e, w))
Dist = [INF] * (D+1)
dijkstra(0, D)
print(Dist[D])