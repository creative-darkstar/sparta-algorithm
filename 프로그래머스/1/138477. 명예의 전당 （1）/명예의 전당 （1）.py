def solution(k, score):
    award = []
    answer = []
    for num in score:
        award.append(num)
        award.sort(reverse=True)
        if len(award) > k:
            award.pop()
        answer.append(award[-1])
    return answer