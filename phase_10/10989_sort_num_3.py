import sys

N = int(sys.stdin.readline())
num_list = [0] * 10001              # 0~100001 까지의 리스트 생성
for _ in range(N):
    num=int(sys.stdin.readline())
    num_list[num] += 1              # 입력받은 수를 index로 +1
for idx in range(len(num_list)):
    if num_list[idx] != 0:          # 1번이라도 나왔으면
        for _ in range(num_list[idx]):      # 그 수만큼 반복해서
            print(idx)                      # 출력
    
'''
# count 정렬 활용하기
N = int(sys.stdin.readline())
num_list = []
for _ in range(N):
    num_list.append(int(sys.stdin.readline()))
# 수를 index로 한 리스트에 1씩 더해서 카운트
index_count = [0 for _ in range(max(num_list)+1)]
for idx in range(len(num_list)):
    index_count[num_list[idx]] += 1
print(index_count)
# 누적합을 통해 인덱스 생성
for idx in range(1,len(index_count)):
    index_count[idx] += index_count[idx -1]
print(index_count)
# index 를 통해 정렬
# num_list 값 -> index -> 위치 검색, index -= 1
result = [0 for _ in range(len(num_list))]
print(result)
for idx in range(len(num_list)-1, -1, -1):
    result[index_count[num_list[idx]]-1] = num_list[idx]
    index_count[num_list[idx]] -= 1
print(result)
'''