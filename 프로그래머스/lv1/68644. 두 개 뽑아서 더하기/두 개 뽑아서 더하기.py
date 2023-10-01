from itertools import combinations

def solution(numbers):
    
    c = list(combinations(numbers,2))
    tmp = []
    for item in c:
        tmp.append(item[0]+item[1])
    tmp.sort()
    answer = list(set(tmp))
    answer.sort()
    
    
    return answer