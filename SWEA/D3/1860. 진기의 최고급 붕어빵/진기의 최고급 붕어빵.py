from collections import defaultdict

t = int(input())
for test_case in range(1, t+1):
    time = 0
    b = 0
    bf = False
    n,m,k = map(int, input().split())
    people_time = list(map(int,input().split()))
    d = defaultdict(int)
    people_time.sort()
    if people_time.count(0) > 0:
        print("#"+str(test_case) + " "+"Impossible")
        continue
    for i in people_time:
        if i == 0:
            continue
        else:
            d[i] += 1
    person_cnt = len(people_time)
    while person_cnt > 0:
        time += 1
        if time % m == 0:
            b += k
        if d[time] != 0:
            if d[time] > b:
                print("#"+str(test_case) + " "+"Impossible")
                bf = True
                break
            else:
                b -= d[time]
                person_cnt -= d[time]
    if not bf:
        print("#"+str(test_case) + " "+"Possible")