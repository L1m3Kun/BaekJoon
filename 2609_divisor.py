# 2609 최대공약수와 최소공배수
input = __import__("sys").stdin.readline


def find_measure(num:int) -> set:
    measure = set()
    for i in range(1, num//2+1):
        if i * (num//i) == num:
            measure.add(i)
            measure.add(num//i)
    return measure


def solution(num1:int, num2:int) -> None:
    m1 = find_measure(num1)
    m2 = find_measure(num2)
    
    return


if __name__ == "__main__":
    num1, num2 = map(int, input().split())
    solution(num1, num2)
