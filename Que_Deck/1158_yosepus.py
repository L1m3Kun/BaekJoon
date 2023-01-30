import sys
from collections import deque

N, k = deque(map(int,sys.stdin.readline().strip().split()))
yoseputh = deque([])
N_lst = [range(1,N+1)]
count = 0
while True:
    if len(N_lst) != 0:
        count += 1
        if count & k == 0:
            yoseputh.append(N_lst.pop(count))
            count == 0
    else:
        break
print(yoseputh)

'''시간초과
import sys
from collections import deque

N, k = deque(map(int,sys.stdin.readline().strip().split()))
yoseputh = deque([])
count = 0
while True:
    if len(yoseputh) != N:
        for idx in range(1, N+1):
            if idx not in yoseputh:
                count += 1
                if count % k == 0:
                    yoseputh.append(idx)
                    count = 0
            else:
                pass
    else:
        break
print(yoseputh)
'''