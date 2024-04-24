def solution(s):
    stack = []
    for c in s:
        stack.append(c)
        if len(stack) > 1:
            if stack[-2] == stack[-1]:
                stack.pop()
                stack.pop()
    
    if len(stack) == 0:
        return 1
    else:
        return 0