def solution(places):
    answer = []
    
    def dis(tmp):
        for i in range(5):
            for j in range(5):
                if tmp[i][j] == "P":
                    stack = []
                    chk=""
                    if i<3:
                        for k in range(1,3):
                            chk+=tmp[i+k][j]
                        stack.append(chk)
                        chk=""
                    if j<3:
                        for k in range(1,3):
                            chk+=tmp[i][j+k]
                        stack.append(chk)
                        chk=""
                    if i>0 and j<4:
                        chk += tmp[i-1][j]
                        chk += tmp[i-1][j+1]
                        stack.append(chk)
                        chk=""
                        chk += tmp[i][j+1]
                        chk += tmp[i-1][j+1]
                        stack.append(chk)
                        chk=""
                    if i<4 and j<4:
                        chk+=tmp[i][j+1]
                        chk+=tmp[i+1][j+1]
                        stack.append(chk)
                        chk=""
                        chk+=tmp[i+1][j]
                        chk+=tmp[i+1][j+1]
                        stack.append(chk)
                        chk=""
                    
                    for val in stack:
                        if val == "OP" or val == "PO" or val == "PP" or val == "PX":
                            return 0
        return 1
        
    for place in places:
        tmp=[]
        for row in place:
            tmp.append(list(row))
        answer.append(dis(tmp))

    return answer