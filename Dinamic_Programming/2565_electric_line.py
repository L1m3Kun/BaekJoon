import sys
input = sys.stdin.readline

N = int(input())
inc = [1] * N
line = {}
# A를 기준으로 B를 정렬
for i in range(N):
    idx, node = map(int, input().split())
    line[idx] = node
line_list = sorted(list(line.keys()))
arr = [line[i] for i in line_list]

# 자르는 전기줄은 가장 긴 증가수열의 개수를 총 개수에서 뺀 값과 같음
max_val = 0
for i in range(N):
    for j in range(i):
        if arr[i] > arr[j]:
            inc[i] = max(inc[i], inc[j] + 1)
    max_val = max(max_val, inc[i])
print(N-max_val)
