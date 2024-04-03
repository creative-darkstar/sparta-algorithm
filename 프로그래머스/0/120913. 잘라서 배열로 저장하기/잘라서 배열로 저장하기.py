def solution(my_str, n):
    length = len(my_str)
    answer = []
    for i in range(length // n + 1):
        if i == length // n:
            sliced = my_str[i * n:]
        else:
            sliced = my_str[i * n:(i + 1) * n]
        if sliced != '':
            answer.append(sliced)
    return answer