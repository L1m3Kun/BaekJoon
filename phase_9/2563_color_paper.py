paper_num = int(input())

paper_list = []
for idx in range(paper_num):
    paper_list.append(list(map(int, input().split())))
paper_area = 300
for num in range(paper_num):
    for idx in range(num + 1, paper_num):
        if (paper_list[idx][0] < paper_list[num][0] < paper_list[idx][0] + 10) and (paper_list[num][1] < paper_list[idx][1] < paper_list[num][1] + 10):   # 왼쪽으로 부터 거리가 n < < n+10 이면서 아래쪽으로부터 n < < n+10 일때
            paper_area -= (paper_list[idx][0] + 10 - paper_list[num][0]) * (paper_list[num][1] + 10 - paper_list[idx][1])

print(paper_area)