import sys

S = sys.stdin.readline().strip()
lst = {}
result=[]
for i in range(97, 123):
    lst[i] = i
s_lst = list(map(chr,S))
for i in range(len(s_lst)):
    for j in range(len(lst)):
        if s_lst[i] == lst[j]:
            result[j] = lst.keys()

