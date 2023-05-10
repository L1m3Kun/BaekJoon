# 8979 올림픽
import sys
input = sys.stdin.readline

N, K = map(int, input().split())
country = [ list(map(int, input().strip().split())) for _ in range(N)]
# 메달 순위 순으로 정렬
country.sort(key=lambda x: (x[1],x[2],x[3]), reverse=1)
rank = same = 1

for i in range(N-1):
    if country[i][0] == K:
        # 만약 원하는 국가에 도달하면 멈추기
        break
    for j in range(1,4):
        if country[i][j] != country[i+1][j]:
            #  다른 메달 개수가 존재할 때 앞에 공동 n의 n을 더해주고 n초기화
            rank+=same
            same = 1
            break
    else:
        # 메달 개수가 모두 같다면 공동 n등 이므로 이를 계산하기 위한 변수 same
        same += 1
print(rank)


