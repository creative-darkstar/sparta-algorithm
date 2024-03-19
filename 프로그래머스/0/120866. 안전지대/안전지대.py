def solution(board):
    n = len(board)
    danger_zone = set()

    for row_idx in range(n):
        for col_idx in range(n):
            if board[row_idx][col_idx] == 1:
                row_start = 0 if row_idx - 1 < 0 else -1
                row_end = 0 if row_idx + 1 > n - 1 else 1
                col_start = 0 if col_idx - 1 < 0 else -1
                col_end = 0 if col_idx + 1 > n - 1 else 1
                for i in range(row_idx + row_start, row_idx + row_end + 1):
                    for j in range(col_idx + col_start, col_idx + col_end + 1):
                        danger_zone.add((i, j))

    return n ** 2 - len(danger_zone)