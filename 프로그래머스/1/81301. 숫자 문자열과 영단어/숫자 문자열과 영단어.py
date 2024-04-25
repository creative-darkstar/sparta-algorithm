def solution(s):
    data_set = {
        "zero": '0',
        "one": '1',
        "two": '2',
        "three": '3',
        "four": '4',
        "five": '5',
        "six": '6',
        "seven": '7',
        "eight": '8',
        "nine": '9',
    }
    answer = ''
    check = ''
    for c in s:
        if c.isdecimal() is True:
            answer += c
        else:
            check += c
            res = data_set.get(check, None)
            if res is not None:
                answer += res
                check = ''

    return int(answer)