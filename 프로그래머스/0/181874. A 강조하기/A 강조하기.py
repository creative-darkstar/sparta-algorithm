def solution(myString):
    answer = ""
    for c in myString:
        if c.lower() == 'a':
            answer += c.upper()
        else:
            answer += c.lower()
    return answer