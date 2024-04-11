def solution(arr):
    answer = [arr[0]]
    comp = arr[0]
    for item in arr[1:]:
        if comp != item:
            answer.append(item)
            comp = item
    return answer