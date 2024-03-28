def solution(arr, queries):
    for query in queries:
        a = query[0]
        b = query[1]
        arr[a], arr[b] = arr[b], arr[a]
    return arr