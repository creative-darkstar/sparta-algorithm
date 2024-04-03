def gcd(num1, num2):
    min_val = min(num1, num2)
    max_val = max(num1, num2)
    for num in range(min_val, 0, -1):
        if max_val % num == 0 and min_val % num == 0:
            return num


def solution(n):
    answer = []
    for i in range(2, n + 1):
        if n % i == 0:
            for num in answer:
                if gcd(i, num) > 1:
                    break
            else:
                answer.append(i)
    return answer