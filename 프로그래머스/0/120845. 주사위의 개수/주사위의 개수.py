def solution(box, n):
    answer = 1
    for edge in box:
        answer *= (edge // n)
    return answer