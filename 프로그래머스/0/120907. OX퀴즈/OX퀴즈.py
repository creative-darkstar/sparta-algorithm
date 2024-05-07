def solution(quiz):
    result = []
    for expression in quiz:
        elements = expression.split()
        if elements[1] == '+':
            if int(elements[0]) + int(elements[2]) == int(elements[4]):
                result.append('O')
            else:
                result.append('X')
        else:
            if int(elements[0]) - int(elements[2]) == int(elements[4]):
                result.append('O')
            else:
                result.append('X')
    return result