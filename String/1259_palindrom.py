# 1259 팰린드롬수
input = __import__("sys").stdin.readline


def solution(s: int) -> str:
    s = str(s)
    if len(s) % 2:
        mid = len(s) // 2
        i, j = mid - 1, mid + 1
        while i >= 0 and j < len(s):
            if s[i] != s[j]:
                return "no"
            i -= 1
            j += 1
    else:
        mid = len(s) // 2
        i, j = mid - 1, mid
        while i >= 0 and j < len(s):
            if s[i] != s[j]:
                return "no"
            i -= 1
            j += 1

    return "yes"


if __name__ == "__main__":
    while True:
        s = int(input())
        if s:
            print(solution(s))
        else:
            break
