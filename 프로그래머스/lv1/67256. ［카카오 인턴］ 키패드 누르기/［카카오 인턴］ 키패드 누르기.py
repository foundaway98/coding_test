


def solution(numbers, hand):
    answer = ''
    keyPad = [["1","4","7","*"],["2","5","8","0"],["3","6","9","#"]]
    li = [0,3]
    ri = [2,3]
    for pushedNumber in numbers:
        numStr = str(pushedNumber)
        if numStr in keyPad[0]:
            answer += "L"
            li = [0,keyPad[0].index(numStr)]
            
        elif numStr in keyPad[2]:
            answer += "R"
            ri = [2, keyPad[2].index(numStr)]
            
        elif numStr in keyPad[1]:
            
            lRowD = max([li[0],1]) - min([li[0],1])
            lColD = max([li[1],keyPad[1].index(numStr)]) - min([li[1],keyPad[1].index(numStr)])
            RRowD = max([ri[0],1]) - min([ri[0],1])
            RColD = max([ri[1],keyPad[1].index(numStr)]) - min([ri[1],keyPad[1].index(numStr)])
            
            if lRowD + lColD < RRowD + RColD:
            
                answer += "L"
                li = [1,keyPad[1].index(numStr)]
            
            elif RRowD + RColD < lRowD + lColD:
            
                answer += "R"
                ri = [1,keyPad[1].index(numStr)]
            
            else:
                if hand == "left":
                    answer += "L"
                    li = [1,keyPad[1].index(numStr)]
                else:
                    answer += "R"
                    ri = [1,keyPad[1].index(numStr)]    
    return answer