"""
10s / 2GB
1,1 출발
행 번호가 작을수록, 열번호가 작을수록 앞에
단어가 목표와 같다면 승리

maps -> n x n

1<= len(maps) = n <=4
1<= len(word) <=4

a -> b -> c
0,2 2,0 [(2,2), (3,3)]

 - - a -
 - - d -
 b - c -
 - - - c
"""

direction = [(1, 0), (0, 1), (-1, 0), (0, -1)]
minV = int(1e9)


def dfs(
    i: int,
    j: int,
    s: list,
    word: str,
    cnt: int,
    visited: list,
    maps: list,
    check_index: dict,
) -> None:
    global minV
    if len(s) == len(word):
        if "".join(s) == word:
            minV = min(cnt, minV)
        return
    if cnt >= minV:
        return
    for di, dj in direction:
        ni, nj = di + i, dj + j
        if 0 <= ni <= len(word) and 0 <= nj <= len(word) and not visited[ni][nj]:
            visited[ni][nj] = 1
            if maps[ni][nj] != "-":
                check_index[maps[ni][nj]] = (ni, nj)
                s.append(maps[ni][nj])
                s.sort(key=lambda x: (check_index[x][1], check_index[x][0]))
                dfs(ni, nj, s, word, cnt + 1, visited, maps, check_index)
                s.pop(s.index(maps[ni][nj]))
            else:
                dfs(ni, nj, s, word, cnt + 1, visited, maps, check_index)
            visited[ni][nj] = 0

    return


def solution(maps: list, word: str) -> int:
    visited = [[0] * len(maps) for _ in range(len(maps))]
    visited[0][0] = 1
    dfs(0, 0, [], word, 0, visited, maps, {})
    answer = minV
    return answer


if __name__ == "__main__":
    # tc1
    # answer : 8
    print(solution(["--a-", "--d-", "b-c-", "---c"], "abc"))
    # tc2
    # answer : -1
    print(solution(["--z", "kye", "-xu"], "zyx"))
    # tc3
    # answer : 0
    print(solution(["a"], "a"))
