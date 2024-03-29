def solution(myStr):
    answer = []
    temp = ""
    
    for c in myStr:
        if c == 'a' or c == 'b' or c == 'c':
            if temp:
                answer.append(temp)
                temp = ""
        else:
            temp += c
    if temp:
        answer.append(temp)
    
    if len(answer) == 0:
        return ["EMPTY"]
    else:
        return answer