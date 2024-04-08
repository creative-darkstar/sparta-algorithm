def solution(sides):
    answer = 0
    # 크기 순으로 나열
    sides.sort()
    for i in range(1, sum(sides)):
        # sides[1]이 가장 긴 변일 경우
        if sides[0] + i > sides[1]:
            answer += 1
        # i가 가장 긴 변일 경우
        elif i >= sides[1]:
            answer += 1
    return answer