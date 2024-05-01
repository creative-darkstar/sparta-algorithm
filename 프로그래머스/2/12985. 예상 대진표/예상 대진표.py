def next_num(n):
    if n % 2 == 1:
        return n // 2 + 1
    else:
        return n // 2


def solution(n, a, b):
    answer = 0
    while True:
        answer += 1
        if abs(a - b) == 1 and min(a, b) % 2 == 1:
            break
        n = n // 2
        a = next_num(a)
        b = next_num(b)

    return answer