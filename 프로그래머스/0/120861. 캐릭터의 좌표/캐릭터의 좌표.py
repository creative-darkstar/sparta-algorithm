def solution(keyinput, board):
    answer = [0, 0]
    x_max = board[0] // 2
    y_max = board[1] // 2
    for k in keyinput:
        if k == "right" and answer[0] < x_max:
            answer[0] += 1
        elif k == "left" and answer[0] > -x_max:
            answer[0] -= 1
        elif k == "up" and answer[1] < y_max:
            answer[1] += 1
        elif k == "down" and answer[1] > -y_max:
            answer[1] -= 1
        else:
            continue
    return answer