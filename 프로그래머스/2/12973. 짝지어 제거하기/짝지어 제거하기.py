def solution(s):
    answer = -1

    test=list(s)
    stack = []
    for item in test:
        if not stack:
            stack.append(item)
            continue
        else:
            stack.append(item)
            if stack[-1] == stack[-2]:
                stack.pop()
                stack.pop()
    if len(stack) == 0:
        answer = 1
    else:
        answer = 0
    
    return answer