def solution(my_string):
    replaced = ""
    for c in my_string:
        if c.isdecimal() is True:
            replaced += c
        else:
            replaced += ' '
    replaced_list = [int(x) for x in replaced.split(' ') if x.isdecimal() is True]
    return sum(replaced_list)