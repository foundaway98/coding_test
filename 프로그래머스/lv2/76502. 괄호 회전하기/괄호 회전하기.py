from collections import deque

def check(curves):
    checker = []
    for curve in curves:
        if len(checker) == 0:
            checker.append(curve)
        elif checker[-1] == "(" and curve == ")":
            checker.pop()
        elif checker[-1] == "{" and curve == "}":
            checker.pop()
        elif checker[-1] == "[" and curve == "]":
            checker.pop()
        else:
            checker.append(curve)
            
    if not checker:
        return True
    else:
        return False

def solution(s):
    s=deque(s)
    answer = 0
    for _ in range(len(s)):
        s.append(s.popleft())
        if check(s):
            answer += 1
    
    
    return answer