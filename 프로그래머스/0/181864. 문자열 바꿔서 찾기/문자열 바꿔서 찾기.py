def solution(myString, pat):
    new = ""
    for c in myString:
        if c == 'A':
            new += 'B'
        else:
            new += 'A'
    return 1 if pat in new else 0