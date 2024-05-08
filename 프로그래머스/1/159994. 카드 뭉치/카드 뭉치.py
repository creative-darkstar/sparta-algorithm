def solution(cards1, cards2, goal):
    for item in goal:
        if not cards1 and not cards2:
            return "No"
        elif not cards1:
            if item == cards2[0]:
                cards2.pop(0)
                continue
            else:
                return "No"
        elif not cards2:
            if item == cards1[0]:
                cards1.pop(0)
                continue
            else:
                return "No"
        else:
            if item == cards1[0]:
                cards1.pop(0)
                continue
            elif item == cards2[0]:
                cards2.pop(0)
                continue
            else:
                return "No" 
    return "Yes"