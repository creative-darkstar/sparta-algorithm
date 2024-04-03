def solution(arr):
    stk = []
    i = 0
    for i in range(len(arr)):
        if len(stk) == 0:
            stk.append(arr[i])
        elif stk[-1] == arr[i]:
            stk.pop()
        elif stk[-1] != arr[i]:
            stk.append(arr[i])
    if len(stk) == 0:
        return [-1]
    else:
        return stk