def solution(names):
    answer = []
    for idx in range(0, len(names), 5):
        answer.append(names[idx])
    return answer