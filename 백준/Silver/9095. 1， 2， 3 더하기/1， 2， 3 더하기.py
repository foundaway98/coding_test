def ott(n):
  if n >= 3:
    return (ott(n-3) + ott(n-2) + ott(n-1))
  elif n == 2:
    return (ott(n-2) + ott(n-1))
  elif n == 1:
    return ott(n-1)
  elif n == 0:
    return 1

cnt = int(input())
testCase = []
for i in range(cnt):
  tmp = int(input())
  testCase.append(tmp)
for i in testCase:
  print(ott(i))