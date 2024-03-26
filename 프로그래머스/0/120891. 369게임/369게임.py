def solution(order):
    answer = 0
    for e in str(order):
        if int(e) % 3 == 0 and e is not '0':
            answer += 1
    return answer