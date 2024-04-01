def solution(s):
    answer = []
    for elem in s.split():
        if elem == 'Z':
            answer.pop()
        else:
            answer.append(int(elem))
    return sum(answer)