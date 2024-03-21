def solution(arr, n):
    length = len(arr)
    start = 0 if length % 2 == 1 else 1
    for idx in range(start, length, 2):
        arr[idx] += n
    return arr