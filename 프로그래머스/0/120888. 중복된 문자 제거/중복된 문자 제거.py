def solution(my_string):
    answer = ''
    temp = list()
    for c in my_string:
        if c not in temp:
            answer += c
            temp.append(c)
    return answer