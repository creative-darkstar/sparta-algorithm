def solution(arr, k):
    n = len(arr)
    answer = []
    idx = 0
    while (idx < n and len(answer) < k):
        if arr[idx] not in answer:
            answer.append(arr[idx])
        idx += 1
    if len(answer) != k:
        answer += [-1] * (k - len(answer))
    return answer