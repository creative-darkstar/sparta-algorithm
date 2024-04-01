def divisors(num):
    num_of_divisors = 0
    for i in range(1, num + 1):
        if num % i == 0:
            num_of_divisors += 1
    return num_of_divisors

def solution(left, right):
    answer = 0
    for i in range(left, right + 1):
        if divisors(i) % 2 == 0:
            answer += i
        else:
            answer -= i
    return answer