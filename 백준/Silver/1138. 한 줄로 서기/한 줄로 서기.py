N = int(input())
people = list(map(int, input().split(" ")))
row = [0] * N

for i in range(N):
  cnt = 0
  for j in range(N):
    if cnt == people[i] and row[j] == 0:
      row[j] = i+1
      break
    elif row[j] == 0:
      cnt += 1
  
print(" ".join(map(str,row)))