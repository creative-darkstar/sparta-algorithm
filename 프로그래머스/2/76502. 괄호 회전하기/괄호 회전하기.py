def is_right_bracket(val):
    stack = []
    brackets = [c for c in val]
    for _ in range(len(brackets)):
        stack.append(brackets.pop(0))
        if len(stack) >= 2:
            if stack[-2] + stack[-1] in ("()", "{}", "[]"):
                stack.pop()
                stack.pop()
    if len(stack) == 0:
        return 1
    else:
        return 0

def solution(s):
    answer = 0
    n = len(s)
    for _ in range(n):
        s = s[-1] + s[:-1]
        answer += is_right_bracket(s)
    return answer