import sys
# 피사노 주기? 그게 뭔데!
# 피보나치 수를 나눌 수를 k라고 할때 k = 10^n이면 피사노주기 = 15*10(n-1)
# a,b = 0,1
# n = int(sys.stdin.readline())
# n %=(15*100000)
# for _ in range(n):
#     a,b = b%1000000, (a+b)%1000000
# print(a)




# 도가뉴 항등식 이용
# F(2n) = F(n)(F(n)+2F(n-1))
# F(2n-1) = F(n)^2 + F(n-1)^2
def fib(n):
    if n == 0:
        return 0
    elif n == 1 or n == 2:
        return 1

    num = n // 2
    fn = fib(num) % 1000000
    fn_1 = fib(num - 1) % 1000000
    if n % 2:   # 홀
        # F(2n-1) = F(n)^2 + F(n-1)^2
        return (fn_1+fn)**2 + fn**2
    else:   # 짝
        # fn_1 = fib(num - 1)%1000000
        # F(2n) = F(n)(F(n+1) + F(n-1))
        return fn * (fn + 2*fn_1)


print(fib(int(sys.stdin.readline()))%1000000)

