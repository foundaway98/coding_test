def solution(n, lost, reserve):
    answer = 0
    # student arr
    students = [1] * n
    for i in lost:
        students[i-1] -= 1
    for i in reserve:
        students[i-1] += 1
    
    for i, student in enumerate(students):
        if student == 0:
            if i-1 == -1:
                #뒤 체크
                if students[i+1] == 2:
                    students[i] += 1
                    students[i+1] -= 1
            elif i+1 == n:
                #앞 체크
                if students[i-1] == 2:
                    students[i] += 1
                    students[i-1] -= 1
            else:
                #앞 또는 뒤 체크
                if students[i-1] == 2:
                    students[i] += 1
                    students[i-1] -= 1
                elif students[i+1] == 2:
                    students[i] += 1
                    students[i+1] -= 1
                
    print(students)
    answer = students.count(1) + students.count(2)
            
    
    return answer