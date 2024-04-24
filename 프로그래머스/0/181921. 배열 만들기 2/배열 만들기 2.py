def bin_to_digit(bin_num):
    return int(str(bin(bin_num))[2:]) * 5


def solution(l, r):
    answer = []

    start_digit = len(str(l)) - 1
    start_bin = 2 ** start_digit
    num = bin_to_digit(start_bin)

    while num <= r:
        if num >= l:
            answer.append(num)
        start_bin += 1
        num = bin_to_digit(start_bin)

    if len(answer) == 0:
        return [-1]
    else:
        return answer