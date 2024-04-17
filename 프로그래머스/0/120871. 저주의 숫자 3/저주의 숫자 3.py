def solution(n):
    answer = 0
    stack = 0
    while stack < n:
        answer += 1
        if not answer % 3 == 0 and '3' not in str(answer):
            stack += 1
    return answer