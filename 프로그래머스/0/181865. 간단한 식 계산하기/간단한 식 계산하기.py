def solution(binomial):
    a, op, b = map(str, binomial.split(' '))
    if op == '+':
        return int(a) + int(b)
    elif op == '-':
        return int(a) - int(b)
    else:
        return int(a) * int(b)