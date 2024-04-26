def dec_to_bin(num, n):
    result = []
    for _ in range(n):
        result.append(num % 2)
        num = num // 2
    return result[::-1]


def solution(n, arr1, arr2):
    answer = []
    for i in range(n):
        tmp = ""
        line_1 = dec_to_bin(arr1[i], n)
        line_2 = dec_to_bin(arr2[i], n)
        for j in range(n):
            if line_1[j] or line_2[j]:
                tmp += '#'
            else:
                tmp += ' '
        answer.append(tmp)

    return answer