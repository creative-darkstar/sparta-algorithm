def solution(arr):
    start = -1
    end = -1
    for idx, item in enumerate(arr):
        if item == 2:
            if start >= 0:
                end = idx
            else:
                start = idx
                end = idx
    if start >= 0:
        return arr[start:end+1]
    else:
        return [-1]