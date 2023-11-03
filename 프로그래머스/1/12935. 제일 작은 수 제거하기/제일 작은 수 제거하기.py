def solution(arr):
    return list(filter(lambda x : x != min(arr), arr)) if len(arr) > 2 else [-1]