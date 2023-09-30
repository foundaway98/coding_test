from itertools import permutations

def solution(k, dungeons):
    
    all = list(permutations(dungeons, len(dungeons)))
    answer = []
    for d in all:
        tired = k
        cnt = 0
        for j in d:
            if tired >= j[0]:
                tired -= j[1]
                cnt += 1
            elif tired < j[0]:
                break
        answer.append(cnt)

    return max(answer)