''' Hint
def recursion(s, l, r):
    if l >= r: return 1
    elif s[l] != s[r]: return 0
    else: return recursion(s, l+1, r-1)

def isPalindrome(s):
    return recursion(s, 0, len(s)-1)

print('ABBA:', isPalindrome('ABBA'))
print('ABC:', isPalindrome('ABC'))
'''
import sys

def recursion(s, l, r, count): # 카운트를 받아 시작
    count += 1  # 1 재귀시 +1
    if l >= r: 
        return 1, count # 마지막 count 출력
    elif s[l] != s[r]: 
        return 0, count
    else: 
        return recursion(s, l+1, r-1,count)

def isPalindrome(s):
    cnt = 0 # 카운트 초기화
    return recursion(s, 0, len(s)-1, cnt)

for test_case in range(int(sys.stdin.readline())):
    test_case = sys.stdin.readline().strip()
    print(*isPalindrome(test_case))