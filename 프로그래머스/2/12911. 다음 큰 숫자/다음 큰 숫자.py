def solution(n):
    answer = 0
    binN = bin(n)
    while True:
        n += 1
        if bin(n)[2:].count("1") == binN.count("1"):
            answer = n
            break
    return answer