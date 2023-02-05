import sys

def hanoi(n, bar1, bar2, bar3):
    if n == 1:
        print(bar1, bar3)
        return
    hanoi(n-1, bar1, bar3, bar2)
    print(bar1, bar3)
    hanoi(n-1, bar3, bar1, bar3)

n = int(sys.stdin.readline())
print(2 ** n - 1)
hanoi(n, 1, 2, 3)





# def hanoi(n, start, finish, arr):
#     if n == 1:
#         arr.append([start, finish])
#         return arr 
#     hanoi(n-1, start, 6- start - finish, arr)
#     arr.append([start, finish])
#     hanoi(n-1, 6- start - finish, finish, arr)
#     return arr

# result = []
# han = hanoi(int(sys.stdin.readline()), 1, 3, result)
# print(len(han))

# for idx in han:
#     print(*idx, sep=" ")






# def hanoi(arr, cnt):
#     if len[arr] == 1:
#         cnt += 1
#         return [1, 3]
#     move = [0,0,0]
#     h = hanoi(arr, cnt)
#     if arr[2] == 0 and arr[1] ==0:
#         arr[0] -= 1
#         arr[2] += 1
#         move.append(h)
#     if arr[1] == 0:


#     return move, cnt

# hanoi_num = []
# for i in range(int(input()), 0, -1):
#     hanoi_num.append(i)