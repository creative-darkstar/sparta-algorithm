def solution(myString):
    tmp = ''
    save = []
    for c in myString:
        if c == 'x':
            if tmp != '':
                save.append(tmp)
                tmp = ''
        else:
            tmp += c
    if tmp != '':
        save.append(tmp)
    save.sort()
    return save