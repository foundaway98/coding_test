from itertools import permutations
import math
def solution(numbers):
    answer = 0
    numlist = []
    allNums = set()
    for i in range(1,len(numbers)+1):
        perList = permutations(numbers,i)
        for perm in perList:
            num = int(''.join(perm))
            allNums.add(num)
    for n in allNums:
        isAnswer = 0
        if n == 0 or n == 1:
            continue
        elif n == 2:
            answer += 1
            continue
        for i in range(2,math.ceil(math.sqrt(n))+1):
            if n%i == 0:
                isAnswer = 1
                break
        if isAnswer == 1:
            continue
        else:
            answer +=1
    return answer