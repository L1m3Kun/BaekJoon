#import sys

# def betrang_theory(n):
#     prime_lst = [False, False] + [True] * (2*n-1)                   # 에라토스테네스의 채

#     for num in range(2, 2*n+1):
#         if prime_lst:
#             for idx in range(num * 2, 2 * n + 1, num):              # 2부터 2n까지의 배수들을 리스트에서 제거
#                 prime_lst[idx] = False
                
    
#     for prime in range(n+1, len(prime_lst)):                        # n 보다 큰 수가 소수일때 count + 1
#         if prime_lst[prime]:
#             count += 1
#     return count
def bertrang_theory(n):
    prime_lst = [0,0] + [1] * (2 * n - 1)    
    for num in range(2, 2*n+1):                           # 에라토스테네스의 채
        if prime_lst[num]:
            for idx in range(num * 2, 2 * n + 1, num):      # 2부터 2n까지의 배수들을 리스트에서 제거
                prime_lst[idx] = 0                      
    return sum(prime_lst[n+1:])
while True:
    n = int(input())
    if n == 0:
        break
    print(bertrang_theory(n))


'''시간초과
while True:
    n = int(input())
    if n == 0:
        break
    prime_lst = [False, False] + [True] * (2*n-1)                   # 에라토스테네스의 채

    for num in range(2, 2*n+1):
        if prime_lst:
            for idx in range(num * 2, 2 * n + 1, num):              # 2부터 2n까지의 배수들을 리스트에서 제거
                prime_lst[idx] = False
                
    count = 0
    for prime in range(n+1, len(prime_lst)):                        # n 보다 큰 수가 소수일때 count + 1
        if prime_lst[prime]:
            count += 1
    print(count)







def betrang_theory(n):
    prime_lst = [False, False] + [True] * (2*n-1)                   # 에라토스테네스의 채

    for num in range(2, 2*n+1):
        if prime_lst:
            for idx in range(num * 2, 2 * n + 1, num):              # 2부터 2n까지의 배수들을 리스트에서 제거
                prime_lst[idx] = False
                
    
    for prime in range(n+1, len(prime_lst)):                        # n 보다 큰 수가 소수일때 count + 1
        if prime_lst[prime]:
            count += 1
    return count

while True:
    n = int(sys.stdin.readline())
    if n == 0:
        break
    print(betrang_theory(n))


def bertrang_theory(n):
    count = 0
    prime_lst = []
    for num in range(n+1, 2*n+1):                           # n보다 크고  2n보다 작거나 같은
        if num in prime_lst:                                # 소수 리스트에 있으면 count +1
            count += 1
        else:                                               # 리스트에 없으면 소수 확인 
            for idx in range(2, int(num**0.5) +1):          # 제곱근까지만 확인
                if num % idx == 0:                          
                    break
            else:                                           # 소수이면 count + 1
                prime_lst.append(num)                       # 소수 저장
                count += 1
    return count
while True:
    n = int(sys.stdin.readline())
    if n == 0:
        break
    print(bertrang_theory(n))



prime_lst =[]
while True:
    n = int(sys.stdin.readline())
    count = 0
    if n == 0:
        break
    for num in range(n+1, 2*n+1):
        if num in prime_lst:
            count += 1
        else:
            for idx in range(2, int(num**0.5) +1):          # 제곱근까지만 확인
                if num % idx == 0:                          
                    break
                else:
                    count += 1
                    prime_lst.append(num)
    print(count)
'''