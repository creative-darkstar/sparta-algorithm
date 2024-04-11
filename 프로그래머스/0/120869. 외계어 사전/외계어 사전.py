def solution(spell, dic):
    answer = 2
    for word in dic:
        if set(spell) == set(word) and len(spell) == len(word):
            answer = 1
    return answer