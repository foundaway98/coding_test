from itertools import permutations
t = int(input())
for test_case in range(1, t+1):
    n = int(input())
    p = list(permutations(list(str(n))))
    f = False
    if n < 10:
        print("#" + str(test_case) + " " + "impossible")
        continue
    for item in p:
        if int("".join(item)) % n == 0:
            if int("".join(item)) == n:
                continue
            else:
                print("#"+str(test_case)+" "+"possible")
                f = True
                break
    if not f:
        print("#"+str(test_case)+" "+"impossible")

