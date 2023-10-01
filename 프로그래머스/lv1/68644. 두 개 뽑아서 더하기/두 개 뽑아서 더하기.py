from itertools import combinations

def solution(numbers):
    
    c = list(combinations(numbers,2))
    tmp = []
    for item in c:
        tmp.append(item[0]+item[1])
    tmp.sort()
    answer = [tmp[0]]
    for item in tmp:
        if item != answer[-1]:
            answer.append(item)
    
    return answer