def solution(arr):
    small = min(arr)
    arr.remove(small)
    return arr if len(arr)>2 else [-1]
    
    # return list(filter(lambda x : x != min(arr), arr)) if len(arr) > 2 else [-1]