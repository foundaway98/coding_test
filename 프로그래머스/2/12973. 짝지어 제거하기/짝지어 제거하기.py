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
    
    return 1 if len(stack) == 0 else 0