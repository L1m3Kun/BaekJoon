x = int(input())
n = int(input())
total_price =0
for _ in range(n):
    a,b = map(int, input().split())
    total_price += a*b
if total_price == x:
    print("Yes")
else:
    print("No")
