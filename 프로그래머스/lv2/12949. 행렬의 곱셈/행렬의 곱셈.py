def solution(arr1, arr2):
    
    answer = []
    
    for m in arr1:
        tmp = []
        for n in range(len(arr2[0])):
            val = 0
            for k in range(len(m)):
                val += m[k] * arr2[k][n]
            tmp.append(val)
        answer.append(tmp)
            
            
    
    return answer