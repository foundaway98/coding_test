from collections import deque
[l, p] = list(map(int,input().split()))
dq = deque(list(range(1,l+1)))
answer = "<"

while dq:
  dq.rotate(-1*(p))
  answer += (str(dq.pop()) + ", ")

answer = answer[:-2] + ">"
print(answer)