import sys

def fib(n):
    if n == 1 or n ==2:
        return 1
    else:
        if n % 2:

# f = fibonacci(int(sys.stdin.readline()))
f = fib(int(sys.stdin.readline()))
print(f%1000000)

