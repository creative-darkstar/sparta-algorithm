def solution(n):
    answer = 0
    for i in range(1, n + 1):
        tmp = i
        sum = 0
        while sum < n:
            sum += tmp
            if sum == n:
                answer += 1
                break
            tmp += 1
    return answer