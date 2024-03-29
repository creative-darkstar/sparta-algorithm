def solution(arr):
    n = len(arr)
    power = 0
    while 2 ** power < n:
        power += 1
    time = 2 ** power - n
    if time == 0:
        return arr
    else:
        for _ in range(time):
            arr.append(0)
        return arr