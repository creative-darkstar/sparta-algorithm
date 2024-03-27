def solution(m, n, board):
    checked = []
    use_board = [] * n
    answer = 0

    for i in range(n):
        tmp = []
        for j in range(m):
            tmp.append(board[m - 1 - j][i])
        use_board.append(tmp)

    while True:
        for i in range(n - 1):
            for j in range(m - 1):
                if use_board[i][j] == use_board[i][j + 1] == use_board[i + 1][j] == use_board[i + 1][j + 1] is not None:
                    checked.append((i, j))

        items = len(checked)

        if items == 0:
            break

        for _ in range(items):
            item = checked.pop()
            i = item[0]
            j = item[1]
            if use_board[i][j] != ' ':
                use_board[i][j] = ' '
                answer += 1
            if use_board[i][j + 1] != ' ':
                use_board[i][j + 1] = ' '
                answer += 1
            if use_board[i + 1][j] != ' ':
                use_board[i + 1][j] = ' '
                answer += 1
            if use_board[i + 1][j + 1] != ' ':
                use_board[i + 1][j + 1] = ' '
                answer += 1

        for i in range(n):
            for j in range(m):
                if use_board[i][j] == ' ':
                    while use_board[i][j] == ' ':
                        del use_board[i][j]
                        use_board[i].append(None)

    return answer