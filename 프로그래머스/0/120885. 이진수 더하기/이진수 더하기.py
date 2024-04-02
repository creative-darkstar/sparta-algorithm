
def solution(bin1, bin2):
    if len(bin1) > len(bin2):
        bin2 = '0' * (len(bin1) - len(bin2)) + bin2
    elif len(bin1) < len(bin2):
        bin1 = '0' * (len(bin2) - len(bin1)) + bin1
    bin1_sep = list(map(int, bin1[::-1].strip()))
    bin2_sep = list(map(int, bin2[::-1].strip()))

    carry = 0
    result = []
    for i in range(len(bin1_sep)):
        cal = carry + bin1_sep[i] + bin2_sep[i]
        digit = cal % 2
        carry = cal // 2
        result.append(digit)
    if carry:
        result.append(carry)

    return ''.join([str(x) for x in result[::-1]])
