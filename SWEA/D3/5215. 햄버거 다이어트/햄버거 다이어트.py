from itertools import combinations
t = int(input())
for test_case in range(1, t+1):
    n, l = map(int, input().split())
    answer = 0
    tasteArr = []
    calArr = []
    for _ in range(n):
        taste, cal = map(int, input().split())
        tasteArr.append(taste)
        calArr.append(cal)
    for i in range(1, n+1):
        c = combinations(range(n), i)
        for idxs in c:
            breakFlag = False
            tastePoint = 0
            calPoint = 0
            for idx in idxs:
                tastePoint += tasteArr[idx]
                calPoint += calArr[idx]
                if calPoint > l:
                    breakFlag = True
                    break
            if not breakFlag:
                if tastePoint >= answer:
                    answer = tastePoint
    print("#"+str(test_case)+" "+str(answer))