def gcd(num1, num2):
    while num2 != 0:
        num1, num2 = num2, num1 % num2
    return num1


def delta(coordinate_01, coordinate_02):
    dx = coordinate_02[0] - coordinate_01[0]
    dy = coordinate_02[1] - coordinate_01[1]
    if dx == 0:
        return [0, dy]
    elif dy == 0:
        return [dx, 0]
    elif dx == 0 and dy == 0:
        return [0, 0]
    else:
        return [dx // gcd(dx, dy), dy // gcd(dx, dy)]


def solution(dots):
    # 각 좌표 x 크기에 따라 자동 정렬
    dots.sort()
    # 가능한 모든 경우의 수
    # case 1: 1, 2 / 3, 4
    # case 2: 1, 3 / 2, 4
    # case 3: 1, 4 / 2, 3
    case_01 = (delta(dots[0], dots[1]), delta(dots[2], dots[3]))
    case_02 = (delta(dots[0], dots[2]), delta(dots[1], dots[3]))
    case_03 = (delta(dots[0], dots[3]), delta(dots[1], dots[2]))
    # case 1의 두 기울기가 같은지 확인
    # 기울기가 같거나 y축에 평행하거나 x축에 평행한 경우
    if case_01[0] == case_01[1] or case_01[0][0] == case_01[1][0] == 0 or case_01[0][1] == case_01[1][1] == 0:
        answer = 1
    # case 2의 두 기울기가 같은지 확인
    # 기울기가 같거나 y축에 평행하거나 x축에 평행한 경우
    elif case_02[0] == case_02[1] or case_02[0][0] == case_02[1][0] == 0 or case_02[0][1] == case_02[1][1] == 0:
        answer = 1
    # case 3의 두 기울기가 같은지 확인
    # 기울기가 같거나 y축에 평행하거나 x축에 평행한 경우
    elif case_03[0] == case_03[1] or case_03[0][0] == case_03[1][0] == 0 or case_03[0][1] == case_03[1][1] == 0:
        answer = 1
    # 모든 경우에 해당하지 않는다면 0
    else:
        answer = 0

    # 상황에 맞게 리턴
    return answer