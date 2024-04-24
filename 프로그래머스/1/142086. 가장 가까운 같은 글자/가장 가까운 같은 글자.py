def solution(s):
    answer = []
    save = dict()
    for idx in range(len(s)):
        if s[idx] not in save.keys():
            answer.append(-1)
            save[s[idx]] = idx
        else:
            answer.append(idx - save[s[idx]])
            save[s[idx]] = idx
    return answer