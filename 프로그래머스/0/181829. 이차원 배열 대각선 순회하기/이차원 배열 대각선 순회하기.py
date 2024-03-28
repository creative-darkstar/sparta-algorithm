def solution(board, k):
    answer = 0
    m = len(board)
    n = len(board[0])
    for i in range(m):
        for j in range(n):
            if i + j <= k:
                answer += board[i][j]
    return answer