def solution(n):
    fib_list = [0, 1]
    num = 2
    while num <= n:
        fib_list.append(fib_list[-2] + fib_list[-1])
        num += 1

    return fib_list[-1] % 1234567