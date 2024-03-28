def solution(arr, queries):
    for query in queries:
        start = query[0]
        end = query[1]
        for idx in range(start, end + 1):
            arr[idx] += 1
    return arr