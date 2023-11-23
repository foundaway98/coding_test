import math

def solution(n, words):
    answer = [0,0]
    spend = []
    for i, word in enumerate(words):
        spend.append(word)
        if len(spend) > 1:
            if (spend[-2][-1] != spend[-1][0]) or spend.index(word) != len(spend) -1 :
                return [n if (i+1) % n == 0 else (i+1) % n, math.ceil((i+1)/n)]

    # [실행] 버튼을 누르면 출력 값을 볼 수 있습니다.

    return answer