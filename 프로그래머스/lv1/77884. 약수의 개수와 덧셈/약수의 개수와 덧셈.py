import math

def solution(left, right):
    def findEvenOrOdd(num):
        cnt = 0
        for i in range(1,num+1):
            if num%i == 0:
                cnt += 1
        if cnt % 2 == 1:
            return True
        else:
            return False
        
    answer = 0
    
    for n in range(left, right+1):
        isOdd = findEvenOrOdd(n)
        if isOdd:
            answer -=n
        else:
            answer +=n
    return answer