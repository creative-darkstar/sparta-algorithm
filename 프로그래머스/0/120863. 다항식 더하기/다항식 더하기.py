def solution(polynomial):
    terms = polynomial.split(" + ")
    poly = [0, 0]
    result = ""
    for term in terms:
        if term[-1] == 'x':
            if len(term) == 1:
                poly[0] += 1
            else:
                poly[0] += int(term[:-1])
        else:
            poly[1] += int(term)
    if poly[0] > 0:
        result += f"{poly[0] if poly[0] > 1 else ''}x"
    if poly[1] > 0:
        if len(result) > 0:
            result += f" + {poly[1]}"
        else:
            result += f"{poly[1]}"
    if poly[0] == 0 and poly[1] == 0:
        result = '0'

    return result