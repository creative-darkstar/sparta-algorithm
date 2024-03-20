def checker(code, word_list):
    check = 0
    if code == '':
        return 1
    for word in word_list:
        if code.find(word) == 0:
            word_list.remove(word)
            check += checker(code[len(word):], word_list)

    return check


def solution(babbling):
    answer = 0
    for code in babbling:
        answer += checker(code, ["aya", "ye", "woo", "ma"])

    return answer