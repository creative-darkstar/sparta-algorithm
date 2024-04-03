def solution(s):
    tmp = sorted([c for c in s], key=lambda x : ord(x), reverse=True)
    return ''.join(tmp)