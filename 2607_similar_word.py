# 2607 비슷한 단어
import sys
from collections import defaultdict

input = sys.stdin.readline

# input
N = int(input())

words = [input().strip() for _ in range(N)]

# define
differ = [defaultdict(int) for _ in range(N)]

cnt = 0
cnt_lst = [0] * N
for s in words[0]:
    differ[0][s] += 1
    for i in range(1, N):
        if s not in words[i]:
            cnt_lst[i] += 1
print(cnt_lst)
for i in range(1, N):
    # for s in words[i]:
    #     differ[i][s] += 1

    # for key, val in differ[i].items():
    #     if key in differ[0].keys():
    #         pass
    tmp = defaultdict(int)
    for s in words[i]:
        tmp[s] += 1

    for s in tmp.keys():
        if s in differ[0].keys():
            if not (differ[0][s] - 1 <= tmp[s] <= differ[0][s] + 1):
                differ[i][s] += abs(tmp[s] - differ[0][s])
            # differ[i][s] += tmp[s]
        else:
            differ[i][s] += tmp[s]

    if differ[i].keys():
        if len(differ[i].keys()) == 1:
            pass
        elif len(differ[i].keys()) == 2:
            pass
    else:
        cnt += 1

print(differ)
