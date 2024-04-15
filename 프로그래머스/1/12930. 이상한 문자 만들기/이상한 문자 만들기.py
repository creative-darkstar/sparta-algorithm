def solution(s):
    answer = ""
    cursor = 0
    for idx in range(len(s)):
        if s[idx] == ' ':
            cursor = 0
            answer += ' '
        else:
            if cursor % 2 == 0:
                answer += s[idx].upper()
            else:
                answer += s[idx].lower()
            cursor += 1
    return answer