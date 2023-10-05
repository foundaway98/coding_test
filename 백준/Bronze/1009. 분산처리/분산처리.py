cnt = int(input())
taskArr = []
for i in range(cnt):
  tmp = list(map(int,input().split(" ")))
  taskArr.append(tmp)
for item in taskArr:
  if item[0] % 10 in [2,3,4,7,8]:
    if item[1] % 4 == 0:
      print(((item[0]%10) ** 4)%10)
    else:
      print(((item[0]%10) ** (item[1] % 4))%10)
  elif item[0] % 10 in [1,5,6]:
    print(item[0] % 10)
  elif item[0] % 10 == 9:
    if item[1] % 2 == 0:
      print(((item[0] % 10) ** 2)%10)
    else:
      print(item[0] % 10)
  else:
    print(10)