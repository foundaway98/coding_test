def solution(s, n):
    answer = ''
    for txt in s:
        if txt == " ":
            answer+=" "
        else:
            if ord(txt)<=90:
                if(ord(txt)+n > 90):
                    answer+=chr(ord(txt)+n-26)
                else:
                    answer+=chr(ord(txt)+n)
            elif ord(txt)>=97 and ord(txt)<=122:
                if(ord(txt) + n > 122):
                    answer+=chr(ord(txt)+n-26)
                else:
                    answer+=chr(ord(txt)+n)

            
    return answer