def solution(price, money, count):
    price_sum = price * (1 + count) * count // 2
    subtract = money - price_sum
    if subtract < 0:
        return -subtract
    else:
        return 0