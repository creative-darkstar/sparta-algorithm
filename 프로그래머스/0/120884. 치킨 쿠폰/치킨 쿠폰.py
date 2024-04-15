def solution(chicken):
    bonus = 0
    chicken_text = str(chicken)
    for i in range(1, len(chicken_text)):
        # 10 단위로 숫자 더하기
        # ex) 1081: 108 + 10 + 1
        bonus += int(chicken_text[:-i])
    # 10 단위로 숫자를 더했을 때 각 일의 자리 숫자들을 모았을 때 10으로 나눈 몫도 더해야 함
    remains = sum([int(c) for c in chicken_text])
    if remains // 10 == 0:
        return bonus
    return bonus + solution(remains)