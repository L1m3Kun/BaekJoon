# 11404 플로이드
import sys
input = sys.stdin.readline


def floyd_warshall(N:int, distance:list):
    # 플로이드-워셜
    # 완전 탐색 1번으로 모든 경우의 수 판단
    for i in range(N): # 경유
        for j in range(N): # 시작
            for k in range(N): # 도착
                # 시작 -> 경유 -> 도착 을 비교하며 최솟값만 저장
                distance[j][k] = min(distance[j][k], distance[j][i] + distance[i][k])
    return distance

def solution():
    # 입력
    N = int(input())
    M = int(input())

    # 최댓값 설정
    limit = 100_001*N

    # 초기 설정
    distance = [[limit] * (N) for _ in range(N)]
    # 나 -> 나  무조건 0
    for i in range(N):
        distance[i][i] = 0 
    # 입력 중 최소만 저장
    for _ in range(M):
        s, e, c = map(int, input().split())
        distance[s-1][e-1] = min(distance[s-1][e-1], c)
    
    # 결과 출력
    ans = floyd_warshall(N, distance)
    for i in range(N):
        for j in range(N):
            if ans[i][j] == limit:
                print(0, end=" ")
            else:
                print(ans[i][j], end= " ")
        print()

if __name__ == "__main__":
    solution()