def solution(lines):
    # 시작점이 line[0]이며 길이가 1인 선분들의 집합
    # ex) 1: 시작점이 1이며 길이가 1인 선분([1, 2])
    set_1 = set([i for i in range(lines[0][0], lines[0][1])])
    set_2 = set([i for i in range(lines[1][0], lines[1][1])])
    set_3 = set([i for i in range(lines[2][0], lines[2][1])])
    # 집합의 연산을 이용하면 중복을 제거하면서 원하는 답을 얻어낼 수 있다.
    return len((set_1 & set_2) | (set_2 & set_3) | (set_3 & set_1))
