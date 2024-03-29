def solution(numbers):
    answer = (0 + 9) * (9 - 0 + 1) // 2
    for num in numbers:
        answer -= num
    return answer