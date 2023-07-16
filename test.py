def turn(matrix, arr):
    si, sj, ei, ej = arr[0]-1, arr[1]-1, arr[2]-1, arr[3]-1
    while True:
        pass
    return matrix
        


def solution(rows, columns, queries):
    answer = []
    matrix = [[0]* columns for _ in range(rows)]
    for i in range(1, rows+1):
        for j in range(1, columns+1):
            matrix[i-1][j-1] = (i-1) * columns + j
    # print(matrix)
    for quest in queries:
        matrix = turn(matrix, quest)

    for i in range(1, rows+1):
        for j in range(1, columns+1):
            if matrix[i-1][j-1] != (i-1) * columns + j:
                answer.append(matrix[i-1][j-1])
    answer.sort()
    return answer

solution(6, 6, [[2,2,5,4],[3,3,6,6],[5,1,6,3]])