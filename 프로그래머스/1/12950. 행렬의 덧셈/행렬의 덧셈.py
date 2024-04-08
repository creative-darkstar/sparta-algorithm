def solution(arr1, arr2):
    answer = []
    m = len(arr1)
    n = len(arr1[0])
    for i in range(m):
        tmp = []
        for j in range(n):
            tmp.append(arr1[i][j] + arr2[i][j])
        answer.append(tmp)
    return answer