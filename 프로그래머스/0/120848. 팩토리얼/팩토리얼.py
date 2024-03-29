def solution(n):
    i = 0
    result = 1
    while n >= result:
        i += 1
        result *= i
    return i - 1