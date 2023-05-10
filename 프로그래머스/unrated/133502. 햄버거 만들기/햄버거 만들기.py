def solution(ingredient):
    answer = 0
    burger=[1,2,3,1]
    tmp = []
    for ing in ingredient:
        tmp.append(ing)
        
        if tmp[-4:] == burger:
            answer+=1
            for j in range(4):
                tmp.pop()
    return answer