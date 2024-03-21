def solution(hp):
    # 장군개미 수만큼 더함
    answer = hp // 5
    # 만약 5의 배수가 아니라면
    if hp % 5 > 0:
    # 정답에 (병정개미 수 + 일개미 수) 를 더함
    # 병정개미 수: (hp % 5)를 3으로 나눈 몫
    # 일개미 수: (hp % 5)를 3으로 나눈 나머지
        answer += ((hp % 5) // 3 + (hp % 5) % 3)
    return answer