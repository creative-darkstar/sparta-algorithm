def solution(s, n):
    answer = ''
    for c in s:
        if c == ' ':
            answer += c
        else:
            if ord(c) >= 97:
                answer += chr(97 + (ord(c) - 97 + n) % 26)
            else:
                answer += chr(65 + (ord(c) - 65 + n) % 26)
    return answer