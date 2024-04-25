def solution(code):
    ret = ""
    mode = 0
    for idx, c in enumerate(code):
        if c == '1':
            if mode == 1:
                mode = 0
            else:
                mode = 1
        else:
            if mode == 0 and idx % 2 == 0:
                ret += c
            elif mode == 1 and idx % 2 == 1:
                ret += c
    
    if not ret:
        return "EMPTY"
    else:
        return ret