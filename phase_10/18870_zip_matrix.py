import sys

N = int(sys.stdin.readline())
x = list(map(int, sys.stdin.readline().strip().split()))
# set으로 중복 삭제
# list형식으로 변환 -> 정렬하여 몇번째로 작은지 설정
index = sorted(list(set(x)))
# dict형식으로 key를 index로, value를 정렬된 순서로 초기화
index_dict ={index[num]: num for num in range(len(index))}
# 입력 x에 대하여 index_dict를 참고하여 값을 출력
print(*[index_dict[num] for num in x])

    

'''시간초과
import sys

N = int(sys.stdin.readline())
x = list(map(int, sys.stdin.readline().strip().split()))
for num in x:
    print(len([i for i in set(x) if i in range(-10**9, num)]), end=" ")
'''



'''시간초과
import sys

N = int(sys.stdin.readline())
x_list = []
x = list(map(int, sys.stdin.readline().strip().split()))
for num in x:
    count = 0
    for idx in x:
        if num > idx:
            count += 1
    x_list.append(count)
print(*x_list)

'''