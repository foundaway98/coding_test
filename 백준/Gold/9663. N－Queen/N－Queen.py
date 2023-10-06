n = int(input())
row = [0]*n
ans = 0

def promising(x):
    for i in range(x):
        if row[x] == row[i] or abs(row[x] - row[i]) == x-i:
            return False
    return True

def nqueen(x):

    global ans

    if x == n:
        ans += 1
        return
    
    else:
        for i in range(n):
            row[x] = i
            if promising(x):
                nqueen(x+1)
nqueen(0)
print(ans)