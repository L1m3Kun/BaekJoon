# 1654 랜선 자르기
import sys
input = sys.stdin.readline

def solution(K:int, N:int, net:list) -> int:
    # 이분탐색
    s, e = 1, max(net)
    m = (s+e)//2
    while s<=e:
        m = (s+e)//2
        cnt = 0
        for line in net:
            cnt += line // m
        if cnt >= N:
            s = m + 1
        else: 
            e = m - 1
    # 마지막에 확인한 값의 s는 최대보다 1큰 숫자일테고,
    # while 문을 통과한 후엔 최대 == e 인 상태가 될 것이기에 e를 출력
    return e        


if __name__ == "__main__":
    K, N = map(int, input().split())
    net = [int(input()) for _ in range(K)]
    print(solution(K, N, net))