import math
from collections import deque

def solution(progresses, speeds):
    days = deque()
    term = []
    answer = [1]
    for i, time in enumerate(progresses):
        days.append(math.ceil((100-time) / speeds[i]))
    while days:
        job = days.popleft()
        if not term:
            term.append(job)
        elif term[-1] >= job:
            answer[-1] += 1
        elif term[-1] < job:
            term.pop()
            term.append(job)
            answer.append(1)
    return answer