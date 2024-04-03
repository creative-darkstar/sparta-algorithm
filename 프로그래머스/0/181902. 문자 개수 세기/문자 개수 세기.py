def solution(my_string):
    answer = [0] * 52
    for c in my_string:
        # 대문자 케이스
        # ord(A) = 97 이므로 71 빼고 시작
        if ord(c) > 96:
            answer[ord(c) - 71] += 1
        # 소문자 케이스
        # ord(a) = 65 이므로 65 빼고 시작
        else:
            answer[ord(c) - 65] += 1
    return answer