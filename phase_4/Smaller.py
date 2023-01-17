n,x = map(int,input().split())
A = list(map(int,input().split()))
for i in A:
    if x > i:
        print(i, end=" ")