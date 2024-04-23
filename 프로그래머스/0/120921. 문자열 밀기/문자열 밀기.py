def solution(A, B):
    turn = 0
    comp = A
    for i in range(len(A)):
        if comp == B:
            return turn
        comp = comp[-1] + comp[:-1]
        turn += 1
    return -1