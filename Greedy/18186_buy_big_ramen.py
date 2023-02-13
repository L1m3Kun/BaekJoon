import sys
N,B,C = map(int,sys.stdin.readline().strip().split())
buy_list = list(map(int, sys.stdin.readline().strip().split()))

cost = 0
if B <=C:
    cost = sum(buy_list) * B
else:
    i = 0
    while i < N:
        if buy_list[i]:
            if i < N-2 and buy_list[i]>0 and buy_list[i+1]>0 and buy_list[i+2]>0 and buy_list[i+1]<=buy_list[i+2]:
                mini = min(buy_list[i], buy_list[i + 1], buy_list[i + 2])
                cost += (B+2*C) * mini
                buy_list[i] -= mini
                buy_list[i + 1] -= mini
                buy_list[i + 2] -= mini
                if buy_list[i]:
                    continue
            elif i < N-2 and buy_list[i]>0 and buy_list[i+1]>0 and buy_list[i+2]>0:
                # mini = min(buy_list[i], buy_list[i + 1])
                cost += B+C
                buy_list[i] -= 1
                buy_list[i + 1] -=1
                if buy_list[i]:
                    continue
            if i < N-1 and buy_list[i]>0 and buy_list[i+1]>0:
                mini = min(buy_list[i], buy_list[i+1])
                cost += (B+C) * mini
                buy_list[i] -= mini
                buy_list[i + 1] -= mini
                if buy_list[i]:
                    continue
            else:
                cost += B * buy_list[i]
            i += 1
        else:
            i += 1
print(cost)