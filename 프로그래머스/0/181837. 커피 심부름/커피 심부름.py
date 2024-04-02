def solution(order):
    answer = 0
    for item in order:
        if "americano" in item:
            answer += 4500
        elif "cafelatte" in item:
            answer += 5000
        else:
            answer += 4500
    return answer