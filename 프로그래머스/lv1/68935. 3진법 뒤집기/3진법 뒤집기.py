def solution(n):
    answer = 0
    three = []
    while True:
        three.append(n%3)
        n = n//3
        if n == 0:
            break
    print(three)
    three.reverse()
    for i, v in enumerate(three):
        answer += three[i] * (3**i)
    
        
        
        
    return answer