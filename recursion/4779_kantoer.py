# 4779 칸토어 집합
import sys

input = sys.stdin.readline


def make_line(start: int, end: int) -> None:
    global lines
    # 길이가 1이면 - 출력
    if end - start <= 1:
        print("-", end="")
        return
    # 1/3 미리 계산
    third = (end - start) // 3
    # 0 ~ 1/3 지점 재 계산
    make_line(start, start + third)
    # 1/3 ~ 2/3 지점은 " "
    print(" " * third, end="")
    # 2/3 ~ 3/3 지점 재 계산
    make_line(start + 2 * third, end)
    return


def solution(N: int) -> None:
    # 하나 끝나고 다음 줄로 넘겨줌
    make_line(0, 3**N)
    print()
    return


if __name__ == "__main__":
    while True:
        # 입력이 있을 때만 실행
        s = input().strip()
        if not s:
            break
        N = int(s)
        solution(N)
