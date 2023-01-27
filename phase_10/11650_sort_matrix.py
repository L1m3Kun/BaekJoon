import sys

N = int(sys.stdin.readline())
matrix_list = []
# 입력 2차원 배열로 정렬
for _ in range(N):
    matrix_list.append(list(map(int, sys.stdin.readline().strip().split())))    
# 출력 요건에 맞춰 리스트 하나씩 리스트 내용 출력
for idx in sorted(matrix_list):
    print(*idx)