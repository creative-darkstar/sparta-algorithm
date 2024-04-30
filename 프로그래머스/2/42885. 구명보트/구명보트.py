def solution(people, limit):
    n = len(people)
    boats = n

    people.sort()

    i = 0
    j = n - 1
    while i != j:
        while j > i:
            if people[i] + people[j] <= limit:
                boats -= 1
                break
            j -= 1
        else:
            break
        i += 1
        j -= 1

    return boats