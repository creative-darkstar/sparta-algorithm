def solution(my_string, indices):
    answer = [c for c in my_string]
    for idx in indices:
        answer[idx] = ''
    return ''.join(answer)