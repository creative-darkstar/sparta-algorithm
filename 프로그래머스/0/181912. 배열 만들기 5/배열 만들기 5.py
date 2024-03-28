def solution(intStrs, k, s, l):
    answer = []
    for item in intStrs:
        comp = int(item[s:s+l])
        if comp > k:
            answer.append(comp)
    return answer