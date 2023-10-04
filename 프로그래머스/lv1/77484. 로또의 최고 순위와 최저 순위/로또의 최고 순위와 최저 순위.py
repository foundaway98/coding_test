def solution(lottos, win_nums):
    matchCnt = 0
    zeroCnt = 0
    matchNum = []
    match = [6,6,5,4,3,2,1]
    for i in lottos:
        if i == 0:
            zeroCnt += 1
        else:
            matchNum.append(i)
    for i in matchNum:
        for j in win_nums:
            if i == j:
                matchCnt += 1
    
    answer = [match[matchCnt],match[matchCnt+zeroCnt]]
    answer.sort()
    
    return answer