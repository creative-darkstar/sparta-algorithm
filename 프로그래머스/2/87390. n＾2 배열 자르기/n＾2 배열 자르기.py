def solution(n, left, right):
    arr = []
    for i in range(left // n + 1, (right // n + 1) + 1):
        for j in range(1, n + 1):
            if j <= i:
                arr.append(i)
            else:
                arr.append(j)
    return arr[(left % n):((right - left) + left % n + 1)]