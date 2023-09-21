def solution(s):
    answer = True
    
    checkArr = []
    for i in s:
        checkArr.append(i)
        if len(checkArr) > 1 and (checkArr[-2] == "(" and checkArr[-1] == ")"):
            checkArr.pop()
            checkArr.pop()
    
        
    
    # [실행] 버튼을 누르면 출력 값을 볼 수 있습니다.
    if len(checkArr) != 0:
        answer = False

    return answer