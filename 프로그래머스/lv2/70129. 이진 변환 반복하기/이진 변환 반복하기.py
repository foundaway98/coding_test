def solution(s):
    global cnt0
    cnt = 0
    cnt0 = 0
    
    while s != "1":
        cnt+=1
        s = changeBinary(s)
    
    return [cnt, cnt0]

def changeBinary(s):
    global cnt0
    cnt0 += s.count("0")
    s = "".join(list(filter(lambda v : v == "1",list(s))))
    binVal = bin(len(s))[2:]
    return binVal