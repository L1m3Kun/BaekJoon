# 좌표이용 하나의 배열만 사용해서 수식 활용
# import sys
#
# def check(start):
#     for i in range(start):
#         if row[start] == row[i] or abs(row[start] - row[i]) == abs(start - i):
#             return 0
#     else:
#         return 1
#
#
# def queen(start, end):
#     if start == end:
#         global count
#         count += 1
#         return
#     else:
#         for j in range(end):
#             row[start] = j
#             if check(start):
#                 queen(start+1, end)
#
#
# N = int(sys.stdin.readline().strip())
# row = [0] * N
# count = 0
# queen(0, N)
# print(count)


# Check 배열
import sys

def check(start, j, end):
    if col[j] or di[start + j] or dj[end - j + start -1]:
        return 0
    else:
        return 1

def queen(start, end):
    if start == end:
        global count
        count += 1
        return
    else:
        for j in range(end):
            if check(start, j, end):
                col[j] = 1
                di[start + j] = 1
                dj[end-1+start-j] = 1
                queen(start+1, end)
                col[j] = 0
                di[start + j] = 0
                dj[end - 1 + start - j] = 0
        return


N = int(sys.stdin.readline().strip())
count = 0
col = [0] * N
di = [0] * (2*N -1)
dj = [0] * (2*N -1)
queen(0,N)
print(count)





# Back - Tracking
import sys
def check(start,j, end):
    for k in range(3):
        ni = start + di[k]
        nj = j + dj[k]
        while 0 <= ni < end and 0 <= nj < end:
            if arr[ni][nj]:
                return 0
            ni += di[k]
            nj += dj[k]
    return 1

def queen(start, end):
    if start == end:
        global count
        count += 1
        return
    else:
        for j in range(end):
            if check(start, j, end):
                arr[start][j] = 1
                queen(start+1, end)
                arr[start][j] = 0
        return 0
# for test_case in range(1, int(input())+1):
N = int(sys.stdin.readline().strip())
    # N = int(input())
arr= [[0] * N for _ in range(N)]
di = [-1, -1, -1]
dj = [-1, 0, 1]
count = 0
queen(0,N)
print(f'#{test_case} {count}')
















#