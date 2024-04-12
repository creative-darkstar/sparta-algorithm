def solution(n):
    answer = 0
    new = []
    digit = 0
    while n > 0:
        new.append(n % 3)
        n = n // 3
    while len(new) > 0:
        answer += new.pop() * (3 ** digit)
        digit += 1
    return answer