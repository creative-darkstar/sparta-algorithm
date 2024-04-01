def solution(array):
    return sum([str(e).count('7') for e in array])