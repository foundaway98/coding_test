cnt = int(input())
pattern = []
for i in range(cnt):
  tmp = input()
  pattern.append(tmp)
checkList = list(pattern[0])

for i in range(1,len(pattern)):
  for c in range(len(checkList)):
    if checkList[c] != pattern[i][c]:
      checkList[c] = "?"
checkList = "".join(checkList)
print(checkList)