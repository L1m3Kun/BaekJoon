import sys

def matrix_multi(arr1, arr2):
    a = len(arr1)
    tmp = [[0 for _ in range(a)] for _ in range(a)]
    for i in range(a):
        for j in range(a):
            for k in range(a):
                tmp[i][j] += (arr1[i][k] * arr2[k][j]) % 1000

    return tmp

def square_mat(arr, n):
    if n == 1:
        return arr
    # if n == 2:
    #     return matrix_multi(arr, arr)
    num = n // 2
    re = square_mat(arr, num)
    if n % 2:
        return matrix_multi(matrix_multi(re,re),arr)
    else:
        return matrix_multi(re, re)


N, B = map(int, sys.stdin.readline().strip().split())
N_list = [list(map(int, sys.stdin.readline().strip().split())) for _ in range(N)]

# for i in range(N):
#     for j in range(N):
#         print(square_mat(N_list, B)[i][j] % 1000, end=" ")
#     print()

# B=1일때 처리 및 언패킹으로 간편화

if B == 1:
    for i in range(N):
        print(*list(map(lambda x: x%1000, [N_list[i][j] for j in range(N)])))
else:
    for i in range(N):
        print(*list(map(lambda x:x%1000, [square_mat(N_list, B)[i][j] for j in range(N)])))