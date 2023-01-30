import sys
# 입력 설정
T = int(sys.stdin.readline())
def prime(n):
    if n == 2:
        return True
    else:
        for idx in range(2,int(n **(1/2)) + 1):
            if n % idx ==0:
                return False
        else:
            return True

for test_case in range(T):
    n = int(input())
    less_half = more_half = n // 2
    while True:
        if prime(less_half) and prime(more_half):
            print(less_half, more_half)        
            break
        elif less_half == 1:
            break
        elif more_half == n:
            break
        less_half -= 1
        more_half += 1