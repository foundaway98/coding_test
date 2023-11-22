import sys
sys.setrecursionlimit(100000)

from collections import defaultdict

def solution(n):
    d = defaultdict(int)
    d[0] = 0
    d[1] = 1
    d[2] = 1
    
    def fibo(n):
        if n == 0 or n == 1 or n == 2:
            return d[n]
        else:
            if not d[n]:
                d[n] = fibo(n-2) + fibo(n-1)
            return d[n]
        
    return fibo(n) % 1234567