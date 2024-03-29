def solution(s):
    answer = []
    for c in s:
        if s.count(c) == 1:
            answer.append(c)
        s.replace(c, '')
    return ''.join(sorted(answer))