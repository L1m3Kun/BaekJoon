import sys
input = sys.stdin.readline

def bf_part(price):
    ram = price // 25

    min_val = price
    for i in range(ram+1):
        num = str(price - 25 * i)
        if len(num) ==2:
            ans = int(num[0])+ int(num[1]) + i
        else:
            ans = int(num) + i
        if min_val > ans:
            min_val = ans 
    return min_val

def dp_part(price):
    n = len(price)
    if n == 1:
        print(int(*price))
        return 
    ans = 0
    if n%2:
        price = ['0'] + price
    for i in range(0,len(price),2):
        ans+=bf_part(int(price[i]+price[i+1]))
    print(ans)
    return

for _ in range(int(input())):
    price = list(input().strip())

    dp_part(price)

    

        



# import sys
# input = sys.stdin.readline


# # def merge_sort(arr):
# #     if len(arr) == 1:
# #         return arr
# #     start = 0
# #     end = len(arr)
# #     mid = (start + end)//2

# #     left = merge_sort(arr[start:mid])
# #     right = merge_sort(arr[mid:end])

# #     i = j = 0
# #     tmp = []
# #     while i < len(left) and j < len(right):
# #         if left[i] <= right[j]:
# #             tmp.append(left[i])
# #         else:
# #             tmp.append(right[j])
# #     if i == len(left):
# #         tmp += right[j:]
# #     if j == len(right):
# #         tmp += left[i:]
# #     return tmp


# def make_coin(price):
#     coin = []
#     for i in range(price):
#         a = b = 0
#         if 10 ** i <= price:
#             coin.append(10 ** i)
#         else:
#             a = 1
#         if 25 * 100 ** i <= price:
#             coin.append(25 * 100 **i)
#         else:
#             b = 1
#         # print('a,b =', a,b)
#         if a and b:
#             break
#     return sorted(coin)


# def counting_coin(price, arr):
#     cnt = 0
#     while price >= 0:
#         if price < 10:
#             cnt += price
#             break
#         num = arr.pop()
#         cnt += price // num
#         price %= num
#         # print('num = ', num)
#         # print('price = ', price)
#         # print('cnt = ', cnt)
#     return cnt


# def solution(num):
#     if num < 10:
#         return num
#     cnt = 0
#     if num < 25:
#         cnt += num // 10 + num % 10
#         return cnt
#     coin = make_coin(num)
#     # print('coin = ',coin)
#     last = coin[-1]
#     dp = [0]*(num//last+1)
#     dp[0] = counting_coin(num, coin[:-1])
#     for i in range(1, num//last+1):
#         pri = num - i*last
#         coin_cnt = counting_coin(pri, coin[:len(coin)-1]) + i
#         dp[i] = min(dp[i-1], coin_cnt)
#         # print('pri = ', pri)
#         # print('coin_cnt = ', coin_cnt)
#     return dp[-1]
    
#         # while num > 0:
#         #     if num < 10:
#         #         cnt += num
#         #         break
#         #     for j in range(num//last):
#         #         num -= last*j
#         #         coin_num = counting_coin(num, coin[:len(coin)-1-j])+j
#         #         dp[i] = min(dp[i], coin_num)
#         #     else:
#         #         pass
#         # dp[i] = min(dp[i-1], dp[i])
#     # return dp[-1]
    
    


# for test_case in range(int(input())):
#     price = int(input())
#     print(solution(price))