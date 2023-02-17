import sys

def calculate(num1,num2, oper):
    if oper == '+':
        return num1 + num2
    elif oper == '-':
        return num1 - num2
    elif oper == '*':
        return num1 * num2
    elif oper == '/':
        if num1 < 0:
            return int(num1/num2)
        else:
            return num1 // num2

def permutation(start, end):
    global minV, maxV
    if start == end:
        result = push_oper(operator, end)
        if maxV < result:
            maxV = result
        if minV > result:
            minV = result
        return
    else:
        for i in range(start, end):
            operator[start], operator[i] = operator[i], operator[start]
            permutation(start+1, end)
            operator[start], operator[i] = operator[i], operator[start]

def push_oper(oper, n):
    result = num[0]
    for j in range(n):
        result = calculate(result, num[j+1], oper[j])
    return result



N = int(sys.stdin.readline().strip())
num = list(map(int, sys.stdin.readline().strip().split()))
oper_num = list(map(int, sys.stdin.readline().strip().split()))

operator = ['+'] * oper_num[0] + ['-'] * oper_num[1] + ['*'] * oper_num[2] + ['/'] * oper_num[3]
stack = []
oper_permu = []
maxV = -10**9
minV = 10**9
permutation(0, len(operator))
print(f'{maxV}\n{minV}')
