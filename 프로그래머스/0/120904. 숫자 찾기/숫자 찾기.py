def solution(num, k):
    for idx, n in enumerate(str(num)):
        if int(n) == k:
            return idx + 1
    return -1