def solution(n):
    arr = [False,False,True]
    for _ in range(3,n+1):
        arr.append(True)
    for i in range(1, len(arr)):
        if arr[i]==True:
            for j in range(i*2, n+1, i):
                arr[j]=False
                
    
    answer=arr.count(True)
    return answer