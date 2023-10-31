# 19637 IF문 좀 대신 써줘
# 보고푼 문제
# 54568 KB 416 ms python
import sys

input = sys.stdin.readline


def solution():
    N, M = map(int, input().split())
    named = []
    check = set([])
    for _ in range(N):
        name, high = input().strip().split()
        # 이미 있는 애들이 넘김
        if int(high) not in check:
            check.add(int(high))
            named.append((name, int(high)))
    for _ in range(M):
        num = int(input())
        # 이분탐색
        left, right = 0, len(named) - 1
        while left <= right:
            mid = (left + right) // 2
            # 네이밍이 오른쪽값을 기준으로 가져가므로 같거나 큰
            if num <= named[mid][1]:
                right = mid - 1
            elif num > named[mid][1]:
                left = mid + 1
        print(named[right + 1][0])


if __name__ == "__main__":
    solution()
