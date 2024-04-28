def solution(arr, query):
    for i, cursor in enumerate(query):
        if i % 2 == 0:
            arr = arr[:cursor+1]
        else:
            arr = arr[cursor:]
    return arr