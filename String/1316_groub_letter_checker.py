import sys

N = int(sys.stdin.readline())
s_list = [sys.stdin.readline().strip() for _ in range(N)]

count = 0

for s in s_list:
    # 단어 하나하나 set에 넣어서 중복이 있으면 break
    stack = set()
    i = 0
    # 중복이 있었는가
    flag = True
    while i < len(s):
        if s[i] not in stack:
            stack.add(s[i])
            i += 1
            # 연속된 단어는 제거
            if i<len(s) and s[i] == s[i-1]:
                for j in range(i, len(s)):
                    if s[j] != s[j-1]:
                        break
                    else:
                        i += 1
        else:
            # 이전에 나왔던 알파벳이면 중지
            flag = False
            break
    # 중복이 없었다면 count +=1
    if flag:
        count += 1
print(count)