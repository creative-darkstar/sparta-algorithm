def solution(arr, queries):
    answer = []
    for query in queries:
        start = query[0]
        end = query[1] + 1
        k = query[2]
        min_val = -1
        for i in range(start, end):
            num = arr[i]
            if num > k and (min_val < 0 or min_val > num):
                min_val = num
        answer.append(min_val)
    return answer