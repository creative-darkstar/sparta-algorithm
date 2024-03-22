def solution(array):
    answer = [0, 0]
    for idx, e in enumerate(array):
        if answer[0] < e:
            answer[0] = e
            answer[1] = idx
    return answer