def solution(a, b, n):
    bottles = 0
    while n > 0:
        new = (n // a) * b
        if new == 0:
            break
        bottles += new
        n = new + n % a

    return bottles