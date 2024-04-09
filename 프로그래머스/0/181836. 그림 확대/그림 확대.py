def solution(picture, k):
    answer = []
    for line in picture:
        new_line = ""
        for pixel in line:
            new_line += pixel * k
        for _ in range(k):
            answer.append(new_line)
    return answer