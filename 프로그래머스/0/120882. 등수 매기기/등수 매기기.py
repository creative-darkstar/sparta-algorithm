def solution(score):
    score_sort = sorted(score, key=lambda x: sum(x), reverse=True)

    grades = []
    grade = 0
    comp = 0
    same = 0
    for s in score_sort:
        if sum(s) == comp:
            same += 1
        else:
            grade += ((same + 1) if same > 0 else 1)
            comp = sum(s)
            same = 0
        grades.append(grade)

    result = []
    for s in score:
        result.append(grades[score_sort.index(s)])

    return result