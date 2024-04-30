def lcd(a, b):
    answer = min(a, b)
    while True:
        if answer % a == answer % b == 0:
            return answer
        answer += 1


def solution(arr):
    if len(arr) == 1:
        return arr[0]
    elif len(arr) == 2:
        return lcd(arr[0], arr[1])
    else:
        tmp = lcd(arr[0], arr[1])
        for num in arr[2:]:
            tmp = lcd(tmp, num)
        return tmp