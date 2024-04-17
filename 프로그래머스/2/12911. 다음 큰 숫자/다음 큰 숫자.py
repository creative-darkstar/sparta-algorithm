def bin_count(num):
    return str(bin(num))[2:].count('1')


def solution(n):
    answer = n + 1
    k = bin_count(n)
    while bin_count(answer) != k:
        answer += 1
    return answer