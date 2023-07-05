# 13144 List of Unique Numbers
import sys
input = sys.stdin.readline

Numbers = [0]*100001

for i in range(1,100001):
    Numbers[i] = Numbers[i-1]+i
# print(Numbers[:5])
left = right = 0

N = int(input())
arr = list(map(int,input().split()))
ans = 0
while left < N:
    print(left, right)
    if left == 0 and right == N-1:
        ans += Numbers[N]
        break
    if len(set(arr[left:right+1])) == (right-left+1):
        right += 1
    else:  
        ans += Numbers[right - left]
        print("ans", ans)
        left += 1
        
print(ans) 