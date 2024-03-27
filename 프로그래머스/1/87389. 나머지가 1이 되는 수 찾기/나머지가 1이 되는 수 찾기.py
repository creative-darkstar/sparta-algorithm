def solution(n):
    answer = 0
    remain = 0
    while remain != 1:
        answer += 1
        remain = n % answer
    return answer