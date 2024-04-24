def solution(brown, yellow):
    # yellow 가로: m, yellow 세로: n
    # brown 개수: 2 * ((m + 1) + (n + 1))
    m_plus_n = (brown // 2) - 2
    n = 1
    m = m_plus_n - 1

    while m * n != yellow:
        n += 1
        m -= 1

    return [m + 2, n + 2]