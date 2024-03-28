def solution(absolutes, signs):
    answer = 0
    for idx, item in enumerate(absolutes):
        if signs[idx] is True:
            answer += item
        else:
            answer -= item
    return answer