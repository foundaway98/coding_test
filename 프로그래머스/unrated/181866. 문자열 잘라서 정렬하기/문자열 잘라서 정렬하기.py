def solution(myString):
    
    answer = myString.split("x")
    answer.sort()
    def isEmpty(item):
        if item == "":
            return False
        return True
    answer = list(filter(isEmpty,answer))
    
    
    return answer