def solution(sizes):
    width = max(map(lambda x: min(x), sizes))
    height = max(map(lambda x: max(x), sizes))
    return width * height