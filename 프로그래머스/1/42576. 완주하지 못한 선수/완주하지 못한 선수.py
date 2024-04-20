from collections import defaultdict

def solution(participant, completion):
    dd = defaultdict(int)
    for p in participant:
        dd[p] += 1
    for c in completion:
        dd[c] += 1
    for k,v in dd.items():
        if v%2 == 1:
            return k
    