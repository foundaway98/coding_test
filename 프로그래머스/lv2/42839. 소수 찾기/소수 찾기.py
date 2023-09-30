from itertools import permutations
def solution(numbers):
    answer = 0
    numlist = []
    allNums = set()
    for i in range(1,len(numbers)+1):
        perList = permutations(numbers,i)
        for perm in perList:
            print(perm)
            num = int(''.join(perm))
            allNums.add(num)
            
    print(allNums)
    
                
            
        
    
    # 조합 생성 후
    
    # 조합된 숫자들 소수 판별
    
    return answer