def solution(arr):
    m = len(arr)
    n = len(arr[0])
    if m > n:
        for item in arr:
            item += [0] * (m - n)
    elif m < n:
        for _ in range(n - m):
            arr.append([0] * n)
    return arr