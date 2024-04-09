def solution(s):
    answer = ""
    is_space = True
    for c in s:
        if c != ' ' and is_space is True:
            is_space = False
            answer += c.upper()
        elif c == ' ':
            is_space = True
            answer += ' '
        else:
            answer += c.lower()
    return answer