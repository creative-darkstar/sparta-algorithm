def solution(numbers, k):
    size = len(numbers)
    # 2 * k - 1: k 번째 홀수
    # % size: 나머지를 이용하여 인덱스를 찾음
    # 1을 빼주는 이유는 리스트 인덱스는 0부터 시작하므로
    return numbers[(2 * k - 1) % size - 1]