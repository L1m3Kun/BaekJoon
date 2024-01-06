# 1676 팩토리얼 0의 개수
import sys
input = sys.stdin.readline


def solution(N:int) -> int:
    if N == 0:
        return 0
    fact = 1
    for i in range(1, N+1):
        fact *= i
    ans = 0
    fact = str(fact)
    for i in range(len(fact)-1, -1,-1):
        if fact[i] != "0":
            return ans
        ans += 1
    


if __name__ == "__main__":
    N = int(input())
    ans = solution(N)
    print(ans)