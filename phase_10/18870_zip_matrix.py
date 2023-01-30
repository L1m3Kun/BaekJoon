import sys


N = int(sys.stdin.readline())
x = list(map(int, sys.stdin.readline().strip().split()))
print(*[sorted(list(set(x))).index(num) for num in x])
# for num in x:
#     print(sorted(list(set(x))).index(num),end = ' ')
    

'''시간초과
import sys

N = int(sys.stdin.readline())
x = list(map(int, sys.stdin.readline().strip().split()))
for num in x:
    print(len([i for i in set(x) if i in range(-10**9, num)]), end=" ")
'''



'''시간초과
import sys

N = int(sys.stdin.readline())
x_list = []
x = list(map(int, sys.stdin.readline().strip().split()))
for num in x:
    count = 0
    for idx in x:
        if num > idx:
            count += 1
    x_list.append(count)
print(*x_list)

'''