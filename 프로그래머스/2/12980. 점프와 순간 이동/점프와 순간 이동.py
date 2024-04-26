def solution(n):
    # 2진수 구한 후 1 개수 세기
    answer = 0
    while n > 0:
        answer += n % 2
        n = n // 2
    return answer