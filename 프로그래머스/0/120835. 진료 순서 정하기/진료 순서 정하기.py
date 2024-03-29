def solution(emergency):
    ranked = sorted(emergency, reverse=True)
    answer = []
    for elem in emergency:
        answer.append(ranked.index(elem) + 1)
    return answer