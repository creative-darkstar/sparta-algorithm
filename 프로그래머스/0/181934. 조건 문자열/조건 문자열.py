def solution(ineq, eq, n, m):
    answer = None
    if ineq == '>':
        if eq == '=':
            answer = (n >= m)
        else:
            answer = (n > m)
    else:
        if eq == '=':
            answer = (n <= m)
        else:
            answer = (n < m)
    return 1 if answer is True else 0