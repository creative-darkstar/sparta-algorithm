# 최적화 이전
"""
def gcd(num1, num2):
    min_val = min(num1, num2)
    max_val = max(num1, num2)
    for num in range(min_val, 0, -1):
        if max_val % num == 0 and min_val % num == 0:
            return num
"""
        
# 최적화
def gcd(num1, num2):
    while num2 != 0:
        num1, num2 = num2, num1 % num2
    return num1


def lcm(num1, num2):
    min_val = min(num1, num2)
    max_val = max(num1, num2)
    for i in range(1, max_val + 1):
        if (min_val * i) % max_val == 0:
            return min_val * i


def solution(numer1, denom1, numer2, denom2):
    denom_sum = lcm(denom1, denom2)
    numer_sum = numer1 * (denom_sum // denom1) + numer2 * (denom_sum // denom2)
    answer = [numer_sum // gcd(numer_sum, denom_sum), denom_sum // gcd(numer_sum, denom_sum)]
    return answer
