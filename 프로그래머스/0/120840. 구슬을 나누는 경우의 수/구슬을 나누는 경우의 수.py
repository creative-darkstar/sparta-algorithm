def solution(balls, share):
    # 분모
    denominator = 1
    # 분자
    numerator = 1
    # nCr
    # n: balls, r: share
    for i in range(share):
        denominator *= (share - i)
        numerator *= (balls - i)

    return numerator // denominator
