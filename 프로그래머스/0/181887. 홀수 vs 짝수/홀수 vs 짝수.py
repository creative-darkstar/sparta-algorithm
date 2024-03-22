def solution(num_list):
    odd = 0
    even = 0
    for idx in range(len(num_list)):
        if idx % 2 == 1:
            odd += num_list[idx]
        else:
            even += num_list[idx]
    return odd if odd >= even else even