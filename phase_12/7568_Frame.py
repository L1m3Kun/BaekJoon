import sys
# 입력
N = int(sys.stdin.readline())
people = [list(map(int, sys.stdin.readline().strip().split())) for _ in range(N)]

# 몸무게와 키가 모두 큰 경우만 카운트해서 출력
for i in range(N):
    frame = 1
    for j in range(N):
        if people[i][0] < people[j][0] and people[i][1] < people[j][1]:
            frame += 1
    print(frame, end=" ")

