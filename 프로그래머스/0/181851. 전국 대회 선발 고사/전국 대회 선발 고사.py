def solution(rank, attendance):
    nums = list()
    r = 1
    while True:
        idx = rank.index(r)
        if attendance[idx] is True:
            nums.append(idx)
        if len(nums) == 3:
            break
        r += 1
    return 10000 * nums[0] + 100 * nums[1] + nums[2]