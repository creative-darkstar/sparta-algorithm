def solution(n, words):
    prev = [words[0]]
    cursor = 1
    while cursor < len(words):
        if words[cursor - 1][-1] != words[cursor][0]:
            return [cursor % n + 1, cursor // n + 1]
        if words[cursor] in prev:
            return [cursor % n + 1, cursor // n + 1]
        prev.append(words[cursor])
        cursor += 1
    return [0, 0]