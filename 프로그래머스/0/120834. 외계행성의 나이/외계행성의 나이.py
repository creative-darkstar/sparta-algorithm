def solution(age):
    # 아스키 코드 97 = 'a'
    # chr(97) = 'a'
    answer = ''.join([chr(97 + int(x)) for x in str(age)])
    return answer