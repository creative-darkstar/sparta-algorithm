def solution(array, n):
    i = 0
    while True:
        if (n - i) in array:
            answer = n - i
            break
        elif (n + i) in array:
            answer = n + i
            break
        i += 1
    return answer