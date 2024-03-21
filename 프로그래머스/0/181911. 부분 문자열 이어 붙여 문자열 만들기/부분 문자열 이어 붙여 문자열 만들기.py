def solution(my_strings, parts):
    answer = ""
    for idx, item in enumerate(parts):
        start, end = item[0], item[1]
        answer += my_strings[idx][start:end+1]
    return answer