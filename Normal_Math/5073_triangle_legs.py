# 5073 삼각형과 세 변
import sys

input = sys.stdin.readline


def check(a: int, b: int, c: int) -> str:
    legs = sorted([a, b, c], reverse=1)
    if legs[0] >= sum(legs[1:]):
        return "Invalid"
    if a == b == c:
        return "Equilateral"
    if a == b or b == c or a == c:
        return "Isosceles"
    return "Scalene"


def solution() -> None:
    while True:
        a, b, c = map(int, input().split())
        if a == b == c == 0:
            break
        print(check(a, b, c))


if __name__ == "__main__":
    solution()
