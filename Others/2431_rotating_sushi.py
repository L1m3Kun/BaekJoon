# 2531 회전초밥
import sys
from collections import deque

input = sys.stdin.readline

N, d, k, c = map(int, input().split())
sushi = [int(input()) for _ in range(N)]
event = []
for i, su in enumerate(sushi):
    if c == su:
        event.append(i)


# def check(lst):
#     if len(lst) == len(set(lst)) and c not in lst:
#         return True
#     return False


start = 0
end = k
lst = deque([*sushi[start:end]])
sushi_list = []
# if check(lst):
#     sushi_list.append((start, end))
while start < N:
    # print(lst, start, end)

    sushi_list.append(
        (start, (end - 1 if end else N - 1), len(set(lst)), (1 if c in lst else 0))
    )
    lst.popleft()
    lst.append(sushi[end])
    if end >= N - 1:
        end = 0
    else:
        end += 1
    start += 1
# print(sushi_list)
ans = 0
# print(event)
for idx in event:
    for sushi_start, sushi_end, length, isContain in sushi_list:
        if not isContain and (
            idx == sushi_end
            or idx + 1 == sushi_start
            or (idx == N - 1 and sushi_start == 0)
        ):
            if ans < length + 1:
                ans = length + 1
        if ans < length:
            ans = length

print(ans)
