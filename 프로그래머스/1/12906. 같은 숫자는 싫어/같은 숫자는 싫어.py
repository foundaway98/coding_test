def solution(arr):
    answer = []
    s = arr[0]
    answer.append(s)
    for i in arr:
        if i == s:
            continue
        else:
            s = i
            answer.append(i)
        
    return answer