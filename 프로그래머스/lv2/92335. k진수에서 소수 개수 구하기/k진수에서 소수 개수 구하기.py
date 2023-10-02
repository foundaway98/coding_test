import math
from collections import deque

def changeNumber(n,k):
    changedNumber = []
    while True:    
        changedNumber.append(n%k)
        n = n//k
        if n == 0:
            break;
    changedNumber.reverse()
    return deque(changedNumber)

def checkPrime(n):
    if n == 1:
        return False
    if n == 2:
        return True
    for i in range(2,math.ceil(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True
        

def solution(n, k):
    answer = 0
    nArr = changeNumber(n,k)
    

    while nArr:
        numStr = ""
        for _ in range(len(nArr)):
            item = nArr.popleft()
            if item == 0:
                break
            else:
                numStr += str(item)
        
        if numStr == "":
            continue
        else:
            if(checkPrime(int(numStr))):
                answer += 1
        
        
        # if isPrime:
        #     answer += 1
        # else:
        #     answer += 0
                
    return answer