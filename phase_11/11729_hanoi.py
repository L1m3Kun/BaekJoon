import sys

def hanoi(arr, cnt):
    if len[arr] == 1:
        cnt += 1
        return [1, 3]
    move = [0,0,0]
    h = hanoi(arr, cnt)
    if arr[2] == 0 and arr[1] ==0:
        arr[0] -= 1
        arr[2] += 1
        move.append(h)
    if arr[1] == 0:


    return move, cnt

hanoi_num = []
for i in range(int(input()), 0, -1):
    hanoi_num.append(i)