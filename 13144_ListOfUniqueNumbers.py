# 13144 List of Unique Numbers
import sys
input = sys.stdin.readline

# print(Numbers[:5])

N = int(input())
arr = list(map(int,input().split()))
Numbers = [0]*(N+1)
for i in range(1,N+1):
    Numbers[i] = Numbers[i-1]+i
left = right = 0
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