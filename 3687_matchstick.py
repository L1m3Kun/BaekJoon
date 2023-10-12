# 3687 성냥개비
import sys

input = sys.stdin.readline

# define
#    숫자    0  1  2  3  4  5  6  7  8  9
# sticks = [6, 2, 5, 5, 4, 5, 6, 3, 7, 6]
sticks = [6, 2, 5, 5, 4, 5, 6, 3, 7, 6]



def saving_num(num, isMin, isFirst):
    if num == 2:
        return 1
    if num == 3:
        return 7
    if num == 4:
        return 4
    if num == 5:
        return 2 if isMin else 5
    if num == 6:
        return (0 if isFirst else 6) if isMin else 9
    if num == 7:
        return 8


def min_num(num):
    i = 7
    lst = []
    cnt = 0
    while i >= 0:
        if num >= i:
            if num - i == 1:
                i -= 1
                continue
            if num - i == 0:
                lst.append(saving_num(i, True, cnt))
                return lst
            num -= i
            lst.append(saving_num(i, True, cnt))
            i = 7
        else:
            i -= 1
        cnt += 1
    if num:
        lst.append(saving_num(num, True, cnt))
    return lst


def max_num(num):
    i = 2
    lst = []
    cnt = 0
    while i <= 7:
        if num >= i:
            if num - i == 1:
                i += 1
                continue
            if num - i == 0:
                lst.append(saving_num(i, False, cnt))
                return lst
            num -= i
            lst.append(saving_num(i, False, cnt))
            i = 2
        else:
            i += 1
        cnt += 1
    if num:
        lst.append(saving_num(num, False, cnt))
    return lst


# testcase
for _ in range(int(input())):
    # input
    num = int(input())
    smallest = min_num(num)
    print(smallest[::-1])
    largest = max_num(num)
    print(largest[::-1])
