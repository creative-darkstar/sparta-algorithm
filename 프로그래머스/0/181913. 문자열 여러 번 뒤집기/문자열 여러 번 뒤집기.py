def solution(my_string, queries):
    for query in queries:
        start = query[0]
        end = query[1]
        rv = my_string[end:start-1:-1] if start > 0 else my_string[end:0:-1] + my_string[0]
        my_string = my_string[:start] + rv + my_string[end+1:]
    return my_string