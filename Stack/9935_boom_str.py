# 9935 문자열 폭발
import sys
input = sys.stdin.readline


def solution(S:str, boom:str) -> str:
    # stack 구조 활용
    stack = []
    # 여러번 호출하는 boom 길이 미리 저장
    len_b = len(boom)
    # 반복 -> stack저장 -> 마지막 len_b까지 문자열이 폭탄이면 pop -> stack 저장
    for i in range(len(S)):
        stack.append(S[i])
        if len(stack) >= len_b and stack[-len_b:] == list(boom):
            for _ in range(len_b):
                stack.pop()
    # 있으면 문자열 없으면 FRULA 출력
    return "".join(stack) if stack else "FRULA"


if __name__ == "__main__":
    print(solution(input().strip(), input().strip()))