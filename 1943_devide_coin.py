# 1943 동전 분배
import sys

input = sys.stdin.readline


# 동전으로 총 금액의 반액 만들기
def make_money_with_coin(coinList: list, coins: dict):
    money = 0

    return 0


# test case
for _ in range(3):
    # define
    coins = {}
    total = 0

    # input
    N = int(input())
    flag = 0
    for i in range(N):
        coin, cnt = map(int, input().split())
        coins[coin] = cnt
        total += coin * cnt
        if cnt % 2:
            flag += 0
        else:
            flag += 1
    if flag == N:
        print(1)
    elif total % 2:
        print(0)
    else:
        total /= 2

        coin_list = list(coins.keys())
        coin_list.sort(reverse=1)
        print(make_money_with_coin(coin_list, coins))

"""
예외 케이스
4
3 7
5 2
7 3
8 1
"""
