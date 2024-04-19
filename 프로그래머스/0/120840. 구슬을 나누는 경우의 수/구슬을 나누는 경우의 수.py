def solution(balls, share):
    answer = 0
    n = 1
    m = 1
    nm = 1
    for a in range(1, balls+1):
        n *= a
    for b in range(1, share+1):
        m *= b
    for c in range(1, balls-share + 1):
        nm *= c
    return n/(nm*m)