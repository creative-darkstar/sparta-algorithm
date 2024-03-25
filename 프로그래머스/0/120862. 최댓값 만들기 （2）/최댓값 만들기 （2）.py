def solution(numbers):
    answer = numbers[0] * numbers[1]
    for n in numbers:
        for m in numbers:
            if n == m:
                continue
            else:
                if answer < n * m:
                    answer = n * m
    return answer