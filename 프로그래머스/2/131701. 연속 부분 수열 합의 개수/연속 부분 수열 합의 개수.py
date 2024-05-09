def solution(elements):
    answer = set()
    for i in range(1, len(elements) + 1):
        if i > 1:
            tmp = elements + elements[:i-1]
        else:
            tmp = elements
        for j in range(len(elements)):
            answer.add(sum(tmp[j:j+i]))
    
    return len(answer)