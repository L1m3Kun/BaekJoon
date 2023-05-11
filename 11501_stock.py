import sys
input = sys.stdin.readline

for _ in range(int(input())):
    N = int(input())
    days = list(map(int, input().split()))
    max_price = days[-1]
    benefit = 0
    for day in range(N-1, -1, -1):
        # 값이 최대일 때만 갱신
        if max_price < days[day]:
            max_price = days[day]
        # 이외엔 이익이니 더하기
        else:
            benefit += max_price-days[day]
    print(benefit)