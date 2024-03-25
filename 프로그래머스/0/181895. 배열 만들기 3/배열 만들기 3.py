def solution(arr, intervals):
    arr_01 = arr[intervals[0][0]:intervals[0][1]+1]
    arr_02 = arr[intervals[1][0]:intervals[1][1]+1]
    return arr_01 + arr_02