# 22866 탑 보기
import sys

input = sys.stdin.readline

N = int(input())
towers = list(map(int, input().split()))
dp = [[] for _ in range(N)]
left_stack = []
right_stack = []

left = 0
right = N - 1
while left < N and right >= 0:
    while left_stack:
        if towers[left_stack[-1]] > towers[left]:
            break
        left_stack.pop()
    dp[left] += left_stack
    left_stack.append(left)
    while right_stack:
        if towers[right_stack[-1]] > towers[right]:
            break
        right_stack.pop()
    dp[right] += right_stack
    right_stack.append(right)

    left += 1
    right -= 1


for i in range(N):
    nearest = 100001
    for j in dp[i]:
        if abs(nearest - i) > abs(i - j):
            nearest = j
        elif abs(nearest - i) == abs(i - j) and nearest > j:
            nearest = j
    print(len(dp[i]), nearest + 1) if dp[i] else print(0)


"""

import sys

input = sys.stdin.readline

N = int(input())
towers = list(map(int, input().split()))

left_cnt = [0] * N
right_cnt = [0] * N
neighber = [[] for _ in range(N)]
max_height_index = 0
last_index = 0
for i in range(N):
    for j in range(i):
        if towers[i] < towers[j]:
            left_cnt[i] = max(left_cnt[i], left_cnt[j] + 1)
print(left_cnt)
for i in range(N - 1, -1, -1):
    for j in range(N - 1, i, -1):
        if towers[i] < towers[j]:
            right_cnt[i] = max(right_cnt[i], right_cnt[j] + 1)
print(right_cnt)

import sys

input = sys.stdin.readline

N = int(input())
towers = list(map(int, input().split()))
for standard in range(N):
    i = j = standard
    maxI = maxJ = towers[standard]
    cnt = 0
    tmp = []
    while True:
        flag_i = False
        flag_j = False
        if i - 1 >= 0:
            i -= 1
            if maxI < towers[i]:
                cnt += 1
                maxI = towers[i]
                tmp.append(i + 1)
        else:
            flag_i = True

        if j + 1 < N:
            j += 1
            if maxJ < towers[j]:
                cnt += 1
                maxJ = towers[j]
                tmp.append(j + 1)
        else:
            flag_j = True

        if flag_j and flag_i:
            break
    print(cnt, end=" ")
    # print(tmp)
    if cnt:
        # minV = 100001
        # index = standard
        # for item in tmp:
        #     if abs(standard - item) < minV:
        #         minV = abs(standard - item)
        #         index = item
        print(tmp[0])
    else:
        print()
"""
