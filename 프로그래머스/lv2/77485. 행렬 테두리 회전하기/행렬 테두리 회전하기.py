def solution(rows, columns, queries):
    answer = []
    #배열 생성
    arr = []
    val = 0
    for i in range(rows):
        temp = []
        for j in range(columns):
            val += 1
            temp.append(val)
        arr.append(temp)
    
    def rotate(idx):
        rowRotatePoint = idx[3]-idx[1]
        colRotatePoint = idx[2]-idx[0]
        
        tmp = []
        for i in range(rowRotatePoint):
            tmp.append(arr[idx[0]-1][idx[1]-1+i])
        for i in range(colRotatePoint):
            tmp.append(arr[idx[0]-1+i][idx[3]-1])
        for i in range(rowRotatePoint):
            tmp.append(arr[idx[2]-1][idx[3]-1-i])
        for i in range(colRotatePoint):
            tmp.append(arr[idx[2]-1-i][idx[1]-1])
        
        tmp.insert(0, tmp.pop())
        tmp.reverse()
        answer.append(min(tmp))
        
        for i in range(rowRotatePoint):
            arr[idx[0]-1][idx[1]-1+i] = tmp.pop()
        for i in range(colRotatePoint):
            arr[idx[0]-1+i][idx[3]-1] = tmp.pop()
        for i in range(rowRotatePoint):
            arr[idx[2]-1][idx[3]-1-i] = tmp.pop()
        for i in range(colRotatePoint):
            arr[idx[2]-1-i][idx[1]-1] = tmp.pop()
        
    for idx in queries:
        rotate(idx)
        
    return answer