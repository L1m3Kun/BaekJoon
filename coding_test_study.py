# 코딩 테스트 공부
def solution(alp, cop, problems):
    answer = 0
    problems.sort(key=lambda x: (x[0], x[1]))
    dp = [
        [225000] * (problems[-1][0] - alp + 1) for _ in range(problems[-1][1] - cop + 1)
    ]
    for i in range(len(dp)):
        for j in range(dp[i]):
            for k in range(len(problems)):
                # if dp[i][j] >
                pass

    return answer


print(solution(10, 10, [[10, 15, 2, 1, 2], [20, 20, 3, 3, 4]]))
print(
    solution(
        0, 0, [[0, 0, 2, 1, 2], [4, 5, 3, 1, 2], [4, 11, 4, 0, 2], [10, 4, 0, 4, 2]]
    )
)
