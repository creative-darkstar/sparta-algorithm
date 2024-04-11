def solution(s):
    stack = []
    cursor = 0
    while cursor < len(s):
        check = s[cursor]
        if check == '(':
            stack.append(check)
        else:
            if len(stack) == 0:
                return False
            else:
                stack.pop()
        cursor += 1
    return True if len(stack) == 0 else False