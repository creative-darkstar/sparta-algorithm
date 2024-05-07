def solution(k, tangerine):
    safe = dict()
    for item in tangerine:
        if str(item) in safe.keys():
            safe[str(item)] += 1
        else:
            safe[str(item)] = 1
    
    arr = sorted(safe.values())
    answer = 1
    while len(arr) > 0:
        if k <= arr[-1]:
            return answer
        else:
            answer += 1
            k -= arr[-1]
            arr.pop()
    
    return answer