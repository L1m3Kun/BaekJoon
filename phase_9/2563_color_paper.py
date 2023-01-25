paper_num = int(input())

paper_list = []
for idx in range(paper_num):
    paper_list.append(list(map(int, input().split())))
total_area = [[0 for _ in range(100)]for _ in range(100)]       # 총 도면

for k in range(len(paper_list)):
    for i in range(10):
        for j in range(10):
            total_area[paper_list[k][0]+i][paper_list[k][1]+j] = 1          # 사각형 색칠 = 1
result = 0
for idx in total_area:
    result += sum(idx)                                                      # 하나당 1면적이므로 1을 모두 더하면 면적
print(result)