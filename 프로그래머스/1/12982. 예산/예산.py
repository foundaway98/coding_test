def solution(d, budget):
    d.sort()
    cnt = 0
    for i in d:
        budget -= i
        cnt += 1
        if budget<0:
            return cnt-1
    return cnt