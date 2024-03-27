def solution(m, n, board):
    # 전체 과정
    # 1. 2x2 사이즈 영역 내에 같은 문자가 있는 경우 index값 별도 저장 (리스트 'checked')
    # 2. 'checked'에 저장해둔 index 값을 확인하며 2x2 사이즈 영역 내의 같은 문자들 모두 공백으로 변경 및 카운팅
    # 3. 공백들 지우면서 요소들 밀어놓기
    # 1 ~ 3을 checked에 요소가 추가되지 않을 때까지 반복
    checked = []    # 2x2 사이즈 영역 같은 문자 확인 시 좌표 값 저장해두는 리스트
    use_board = []  # 1 ~ 3 과정 진행을 위해 board를 시계 방향으로 90도 회전하여 저장하는 2차원 리스트
    answer = 0      # 리턴값

    # 전체 과정을 진행하기 위해 use_board 정의
    # use_board는 board를 시계 방향으로 90도 회전한 것
    for i in range(n):
        tmp = []
        for j in range(m):
            tmp.append(board[m - 1 - j][i])
        use_board.append(tmp)
    
    # 1 ~ 3 반복
    while True:
        # 1. 2x2 사이즈 영역 내에 같은 문자가 있는 경우 index값 별도 저장 (리스트 'checked')
        for i in range(n - 1):
            for j in range(m - 1):
                if use_board[i][j] == use_board[i][j + 1] == use_board[i + 1][j] == use_board[i + 1][j + 1] is not None:
                    checked.append((i, j))
        
        # checked의 요소 개수
        items = len(checked)
        # 반복 중단 조건 체크. 2x2 사이즈 영역 같은 문자 없을 시 종료
        if items == 0:
            break
        
        # 2. 'checked'에 저장해둔 index 값을 확인하며 2x2 사이즈 영역 내의 같은 문자들 모두 공백으로 변경 및 카운팅
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

        # 3. 공백들 지우면서 요소들 밀어놓기
        for i in range(n):
            for j in range(m):
                if use_board[i][j] == ' ':
                    while use_board[i][j] == ' ':
                        del use_board[i][j]
                        use_board[i].append(None)

    return answer