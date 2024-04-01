def solution(strArr):
    answer = dict()
    for item in strArr:
        if len(item) in answer.keys():
            answer[len(item)] += 1
        else:
            answer[len(item)] = 1
    return max(answer.values())