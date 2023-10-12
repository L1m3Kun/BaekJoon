# 3758 KCPC
import sys
from collections import defaultdict

input = sys.stdin.readline

for _ in range(int(input())):
    # input
    # 팀 개수, 문제 개수, 내 팀 id, 로그 엔트리
    n, k, t, m = map(int, input().split())
    # define
    # 아이디별 {제출횟수, 마지막 제출 시간, 문제별 점수(list)}
    score = {}
    rank = []
    # score = defaultdict(list(int, int, list(int)))
    for idx in range(m):
        i, j, s = map(int, input().split())
        if i in score.keys():
            sub_cnt, _, scores = score[i]
            # print(sub_cnt, _, scores)
            scores[j] = scores[j] if scores[j] >= s else s
            score[i] = [sub_cnt + 1, idx, scores]
        else:
            scores = defaultdict(int)
            scores[j] = s
            score[i] = [1, idx, scores]
            # print(score[i])

    # 내 점수
    my_score = sum(score[t][2].values())
    # print("my score is ", my_score)
    for key, val in score.items():
        # print("val", val[2].values())
        # if key != t:
        rank.append((key, sum(val[2].values())))
    rank.sort(reverse=1, key=lambda x: (x[1], -score[x[0]][0], -score[x[0]][1]))
    # print("rank is", rank)
    # print(score)
    for i in range(len(rank)):
        if my_score > rank[i][1]:
            print(i + 1)
            # answer = i
            break
        elif my_score == rank[i][1]:
            if score[rank[i][0]][0] > score[t][0]:
                # answer = i
                print(i + 1)
                break
            elif score[rank[i][0]][0] == score[t][0]:
                if score[rank[i][0]][1] >= score[t][1]:
                    # answer = i
                    print(i + 1)
                    break
    else:
        print(len(rank) + 1)
        # answer = len(rank) - 1
    # print(answer + 1)
