import sys

s = sys.stdin.readline().strip()
result = set()
# indexing으로 길이 늘려가며 set에 추가(중복제거)
for i in range(len(s)):
    for j in range(i+1,len(s)+1):
        result.add(s[i:j])
print(len(result))