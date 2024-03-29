def solution(myString, pat):
    answer = 0
    cursor = -1
    while True:
        cursor = myString.find(pat, cursor + 1)
        if cursor == -1:
            break
        else:
            answer += 1
    return answer