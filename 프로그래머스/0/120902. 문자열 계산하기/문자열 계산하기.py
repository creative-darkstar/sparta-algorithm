def solution(my_string):
    answer = 0
    characters = my_string.split()
    is_plus = True
    is_minus = False

    print(characters)
    for c in characters:
        if c == '+':
            is_plus = True
        elif c == '-':
            is_minus = True
        else:
            tmp = int(c)
            if is_plus is True:
                answer += tmp
                is_plus = False
            elif is_minus is True:
                answer -= tmp
                is_minus = False

    return answer