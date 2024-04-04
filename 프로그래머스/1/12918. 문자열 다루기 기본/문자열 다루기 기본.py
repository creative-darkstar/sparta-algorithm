def solution(s):
    n = len(s)
    if not (n == 4 or n == 6):
        return False
    try:
        answer = int(s)
        return True
    except:
        return False