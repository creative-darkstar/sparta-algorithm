def solution(name, yearning, photo):
    person_yearning = dict()
    for idx in range(len(name)):
        person_yearning[name[idx]] = yearning[idx]
    
    answer = []
    for people in photo:
        sum_yearning = 0
        for person in people:
            sum_yearning += person_yearning.get(person, 0)
        answer.append(sum_yearning)
    
    return answer