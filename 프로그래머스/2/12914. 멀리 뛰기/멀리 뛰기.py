def combination(n, r):
    if r == 0 or r == n:
        return 1
    else:
        numer = 1
        denom = 1
        for i in range(r):
            numer *= (n - i)
            denom *= (r - i)
        return numer // denom


def solution(n):
    answer = 0
    r = 0
    
    while n >= r:
        answer += combination(n, r)
        n -= 1
        r += 1

    return answer % 1234567