def solution(a, d, included):
    n = len(included)
    answer = 0
    for idx, num in enumerate(range(a, a + n * d, d)):
        if included[idx] is True:
            answer += num
    return answer