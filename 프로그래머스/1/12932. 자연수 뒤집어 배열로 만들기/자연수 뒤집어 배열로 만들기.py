def solution(n):
    temp = [c for c in str(n)]
    n = len(temp)
    answer = []
    for i in range(n):
        answer.append(int(temp.pop()))
    return answer