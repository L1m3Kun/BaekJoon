M,N = map(int, input().split())

def Prime(n):
    lst = [0,0]+[1]*(n-2)
    for i in range(2,n**0.5+1):
        for j in range(i+1, n**0.5+1):
            if n % (i * j) == 0:
                lst.remove(i*j)
    