import sys
# set 이용, 메모리 더먹음, 속도 빠름
# 입력
N = int(sys.stdin.readline())
sanggen = set(map(int, sys.stdin.readline().strip().split()))
M = int(sys.stdin.readline())
ispair = list(map(int, sys.stdin.readline().strip().split()))

sanggen_list = ['0'] * M

for idx in range(M):
    if ispair[idx] in sanggen:
        sanggen_list[idx] = '1'
print(" ".join(sanggen_list))




''' 선택 알고리즘 활용, 메모리 덜 먹음
# 내부에 있는가를 확인하기 위한 선택 알고리즘
def selection(arr, key):
    start = 0
    end = len(arr) - 1
    while start <= end:
        c = (start+end) // 2
        if arr[c] == key:
            return 1
        elif arr[c] < key:
            start = c + 1
        else:
            end = c - 1
    return 0
# 입력, 선택 알고리즘을 사용하기 위한 sorting
N = int(sys.stdin.readline())
sanggen = list(map(int, sys.stdin.readline().strip().split()))
sanggen.sort()

M = int(sys.stdin.readline())
ispair = list(map(int, sys.stdin.readline().strip().split()))

# dictionary에 저장, 중복 제거하여 수행 -> 실행시간 빨라짐
index = list(set(ispair))

card_dict = {}

for idx in index:
    card_dict[idx] = selection(sanggen, idx)
# 출력
print(*[card_dict[i] for i in ispair])
'''