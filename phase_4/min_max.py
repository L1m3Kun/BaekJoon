n=int(input())
arr = list(map(int,input().split()))
max = -1000000
min = 1000000
for i in arr:
    if i >= max:
        max = i
    elif i < min:
        min = i
print(min,max)
