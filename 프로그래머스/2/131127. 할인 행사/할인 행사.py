def solution(want, number, discount):
    answer = 0
    
    for idx, num in enumerate(number):
        for _ in range(num - 1):
            want.append(want[idx])
    
    for i in range(0, len(discount) - 9):
        if i == len(discount) - 10:
            if sorted(want) == sorted(discount[i:]):
                print(i)
                answer += 1
        else:
            if sorted(want) == sorted(discount[i:i+10]):
                print(i)
                answer += 1
    
    return answer