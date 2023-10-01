from collections import deque

def solution(s):
    numTable = ['0','1','2','3','4','5','6','7','8','9']
    engTable = ['zero','one','two','three','four','five','six','seven','eight','nine']
    s = deque(s)
    answer = []
    convert = ""
    
    while len(s) != 0:
        item = s.popleft()
        if item in numTable:
            answer.append(item)
        else:
            convert += item
            
            if convert in engTable:
                answer.append(str(engTable.index(convert)))
                convert = ""

    answer = int("".join(answer))
    return answer