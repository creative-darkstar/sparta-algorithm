def solution(arr, delete_list):
    for item in delete_list:
        if item in arr:
            arr.remove(item)
    return arr