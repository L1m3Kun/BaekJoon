# 1138 한 줄로 서기
'''
1<= N <=10 자연수
(리스트 내부 수) <= N
'''

import sys
input = sys.stdin.readline

# Input
N = int(input())
arr = list(map(int,input().split()))

# Define
# 정답 만들기 용 리스트
line = [0] * N

# Setting Line Function
def Insert_Number(start:int, end:int, num:int):
    for i in range(start,end):
        if not line[i]:
            line[i] = num
            return 

# Main
def Main():               
    for i in range(N):
        cnt = 0
        for j in range(N):
            if cnt == arr[i]:   # 나보다 키가 큰 사람이 입력 받은 만큼 있으면
                Insert_Number(j, N, i+1) # 빈 곳에 서기
                break                       #  다음 사람의 순서로 가기위해 break
            elif not line[j] or line[j] >= (i+1):   # 아직 나보다 큰 사람들이 입력받은 만큼 없는 경우,
                cnt += 1                    # 키가 큰 사람이 있거나, 큰 사람이 설 가능성이 있는 경우 카운트
    print(*line)


Main()      