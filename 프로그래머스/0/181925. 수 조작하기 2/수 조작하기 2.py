def solution(numLog):
    answer = ''
    for i in range(1, len(numLog)):
        ctrl = numLog[i] - numLog[i - 1]
        if ctrl == 1:
            answer += 'w'
        elif ctrl == -1:
            answer += 's'
        elif ctrl == 10:
            answer += 'd'
        else:
            answer += 'a'
    return answer