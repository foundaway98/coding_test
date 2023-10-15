def solution(x):
    forSum = list(str(x))
    s = 0
    for i in forSum:
        s += int(i)
    return x % s == 0