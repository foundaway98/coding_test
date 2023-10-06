tmp = list(map(int,input().split(" ")))
row = tmp[0]
col = tmp[1]

table = []
for i in range(row):
  tmp = input()
  table.append(tmp)

def findSquare(s):
  for i in range(row-s+1):
    for j in range(col-s+1):
      if table[i][j] == table[i][j+s-1] == table[i+s-1][j] == table[i+s-1][j+s-1]:
        return True
  return False

size = min(row, col)
for k in range(size,0,-1):
  if findSquare(k):
    print(k**2)
    break