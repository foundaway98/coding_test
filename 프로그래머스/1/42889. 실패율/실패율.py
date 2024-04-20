from collections import defaultdict

def solution(N, stages):
    answer = []
    dd = defaultdict(int)
    for i in stages:
        dd[i] += 1
    f = []
    for i in range(1,N+1):
        if dd[i] == 0:
            f.append(0)
        else:
            people = 0
            for j in range(i, N+2):
                people+=dd[j]
            f.append(dd[i]/people)

    for i in list(reversed(sorted(f))):
        answer.append(f.index(i) + 1)
        f[f.index(i)] = 1
        
    
    return answer