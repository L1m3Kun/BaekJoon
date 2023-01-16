import sys
T = int(input())
for test_case in range(1,T+1):
    a,b = map(int, sys.stdin.readline().split())
    print(f"Case #{test_case}: {a+b}")