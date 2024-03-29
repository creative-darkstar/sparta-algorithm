def solution(arr):
    min_val = min(arr)
    while min_val in arr:
        arr.remove(min_val)
    if len(arr) == 0:
        return [-1]
    else:
        return arr