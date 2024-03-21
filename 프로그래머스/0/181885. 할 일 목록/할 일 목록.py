def solution(todo_list, finished):
    answer = []
    for idx in range(len(finished)):
        if finished[idx] is False:
            answer.append(todo_list[idx])
    
    return answer