def gcd(num1, num2):
    while num2 != 0:
        num1, num2 = num2, num1 % num2
    return num1


def solution(a, b):
    b = b // gcd(a, b)
    while b % 2 == 0 or b % 5 == 0:
        if b % 2 == 0:
            b = b // 2
        if b % 5 == 0:
            b = b // 5
    return 1 if b == 1 else 2