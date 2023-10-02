def solution(n, left, right):
    # index 와 숫자 사이의 관계 : index // n과 index % n 중 큰 수에 + 1을 한 것과 같다
    matrix = []
    answer = []
    for num in range(left, right+1):
        row = num//n + 1
        col = num%n + 1
        matrix.append([row, col])
    
    for mat in matrix:
        answer.append(max(mat[0], mat[1]))

    return answer