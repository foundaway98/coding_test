def solution(brown, yellow):
    
    
    answer = []
    for i in range(1,brown*yellow):
        x=i
        y=(brown+4)/2-x
        if(x-2)*(y-2) == yellow:
            answer = [x,y]
            answer.sort(reverse=True)
            return answer
    
    return answer