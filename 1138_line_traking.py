# 1138 한 줄로 서기
import sys
input = sys.stdin.readline

N = int(input())
line = [0] * N
arr = list(map(int,input().split()))

for height_index in range(N):
    big_cnt = idx_cnt = 0
    for idx in range(N):
        
        
print(*line)