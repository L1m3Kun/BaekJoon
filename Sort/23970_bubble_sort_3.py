import sys


def bubble_sort(arr1, arr2, length):
    # 처음부터 같으면 바로 출력
    if arr1 == arr2:
        return 1
    else:
        for last in range(length-1, 0, -1):
            for idx in range(last):
                if arr1[idx] > arr1[idx+1]:
                    arr1[idx], arr1[idx+1] = arr1[idx+1], arr1[idx]
                    # 바꿨을 때 부분적으로 같으면 전체 비교
                    if arr1[idx] == arr2[idx] and arr1[idx+1] == arr2[idx+1]:
                        if arr1 == arr2:
                            return 1
        return 0


N = int(sys.stdin.readline())
N_arr1 = list(map(int, sys.stdin.readline().strip().split()))
N_arr2 = list(map(int, sys.stdin.readline().strip().split()))

print(bubble_sort(N_arr1, N_arr2, N))