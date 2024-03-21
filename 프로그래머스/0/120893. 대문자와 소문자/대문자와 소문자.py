def solution(my_string):
    answer = ''
    for c in my_string:
        if c.islower() == True:
            answer += c.upper()
        else:
            answer += c.lower()
    return answer