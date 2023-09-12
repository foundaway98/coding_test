def toUpperCase(word):
    wordHead = word[:1]
    wordTail = word[1:]
    if(not isinstance(wordHead, int)):
        wordHead = wordHead.upper()
    wordTail = wordTail.lower()
    newWord = wordHead + wordTail
    return newWord

def solution(s):
    arr = list(s.split(" "))
    answer = ""
    print(arr)
    for item in arr:
        if item != "":
            answer = answer + toUpperCase(item) + " "
        else:
            answer += " "
    
    return answer[:-1]