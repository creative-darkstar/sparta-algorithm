def solution(arr, flag):
    answer = []
    for idx, item in enumerate(flag):
        if item is True:
            for _ in range(arr[idx] * 2):
                answer.append(arr[idx])
        else:
            for _ in range(arr[idx]):
                answer.pop()
    return answer