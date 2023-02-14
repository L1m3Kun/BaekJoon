import sys
from collections import deque

N, k = deque(map(int,sys.stdin.readline().strip().split()))
# <<<<<<< HEAD
count = 1
# =======

# 수학적 개념으로 풀기

lst = list(range(1, N+1))
joseputh = []
count = 1
while len(joseputh) != N:
    if count % k == 0:
        if count > N:
            print(count)
            joseputh.append(lst.pop(count%N))
            print(joseputh)
            count %= N
        else:
            joseputh.append(lst.pop(count))
    count += 1
print(joseputh)
        
     


''' deque 개념으로 풀기
import sys
from collections import deque

N, k = deque(map(int,sys.stdin.readline().strip().split()))
yoseputh = deque(range(1, N+1))
result = []
count = 1
while True:
    # result 가 N개 될때까지
    if len(result) != N:
        # 왼쪽에서 하나씩 빼서 다시 오른쪽으로 넣음
        k_idx = yoseputh.popleft()
        if count % k == 0:  # 카운트가 k번째마다
            result.append(k_idx)    #result로 숫자빼돌림
        else:
            yoseputh.append(k_idx)
        count += 1
    else:
        break
print('<', end='')
print(*result, end='',sep= ', ')
print('>')
'''
'''시간초과
import sys
from collections import deque

N, k = deque(map(int,sys.stdin.readline().strip().split()))
>>>>>>> abbebad847dd18765efb5f47f56350cca5706a80
yoseputh = deque([])
while True:
<<<<<<< HEAD
    if len(yoseputh) != N:
        
        if count == N:
            count = 1
        else:
            count += 1
=======
    if len(N_lst) != 0:
        count += 1
        if count & k == 0:
            print(count)
            if count > N:
                yoseputh.append(N_lst.pop(count-N-1))
                count = 0
            else:
                yoseputh.append(N_lst.pop(count-1))
>>>>>>> abbebad847dd18765efb5f47f56350cca5706a80
    else:
        break
print(yoseputh)


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