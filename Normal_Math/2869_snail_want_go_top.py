# 2869 달팽이는 올라가고 싶다
input = __import__("sys").stdin.readline


def solution(A: int, B: int, V: int) -> int:
    day = V // (A - B)
    print(day)
    if (day - 1) * (A - B) + A >= V:
        return day
    if day * (A - B) + A >= V:
        return day + 1


if __name__ == "__main__":
    print(solution(*list(map(int, input().split()))))
