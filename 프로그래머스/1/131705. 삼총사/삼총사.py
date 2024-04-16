def solution(number):
    def generate(chosen, start=0):
        answer = 0
        if len(chosen) == 3:
            if sum(chosen) == 0:
                return 1
            else:
                return 0
        for idx in range(start, len(number)):
            chosen.append(number[idx])
            answer += generate(chosen, start=(idx + 1))
            chosen.pop()
        return answer

    return generate([])