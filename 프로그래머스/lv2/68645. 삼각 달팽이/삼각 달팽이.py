def solution(n):
    arr=[[0 for i in range(n)] for j in range(n)]
    num = 0
    x = 0
    y = 0
    step = 0
    answer = []
    for i in range(n,0,-1):
        step+=1
        for j in range(i):
            num += 1
            if (step % 3 == 1):
                arr[x+j][y]=num
            elif(step%3 == 2):
                arr[x][y+j]=num
            elif(step%3==0):
                arr[x-(j)][y-(j)]=num
                
        if (step%3==1):
            x = x+(i-1)
            y += 1
        elif(step%3==2):
            y = y + i - 2
            x = x - 1
        elif(step % 3 == 0):
            x = x-(i-1)+1
            y = y-(i-1)
        
    for i in arr:
        for j in i:
            if j != 0:
                answer.append(j)

    return answer