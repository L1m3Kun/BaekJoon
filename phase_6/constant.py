comp_lst = list(map(int,input().split()))

def reverse(n):                 # 뒤집어!
    tmp = n
    total = 0
    for i in range(3):
        dem = tmp % 10              # 나머지
        tmp = tmp // 10             # 몫
        total += dem * 10**(2-i)    # 나머지를 100, 10, 1 을 각각 곱해 더함
    return total

print(max(reverse(comp_lst[0]),reverse(comp_lst[1])))
        