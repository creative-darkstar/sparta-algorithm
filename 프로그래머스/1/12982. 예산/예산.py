def solution(d, budget):
    d.sort(reverse=True)
    answer = 0
    s = 0
    while s < budget:
        if len(d) == 0:
            break
        s += d.pop()
        if s > budget:
            break
        answer += 1
    return answer