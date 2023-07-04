# 2075 N번째 큰 수
import sys
import heapq
input = sys.stdin.readline

N = int(input())
arr = [list(map(int, input().strip().split())) for _ in range(N)]

maxIndex = [N-1] * N

que = []
for i in N:
    heapq.heappush(que, arr[i][maxIndex])

for _ in range(N):
    pass